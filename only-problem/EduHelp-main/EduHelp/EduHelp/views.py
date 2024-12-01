from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.shortcuts import redirect,render,get_object_or_404
from django.contrib.auth.models import User
from products.models import Course

def base(request):
    return render(request,'base.html')

def index(request):
    return render(request, 'index.html')

def home(request):
    popular_courses = Course.objects.order_by('-created_at')[:3]  # Latest 3 courses
    all_courses = Course.objects.all()  # All courses
    return render(request, 'home.html', {
        'popular_courses': popular_courses,
        'all_courses': all_courses,
    })

def course(request):
    courses = Course.objects.all()
    return render(request,'components/course.html',{
        'courses':courses,
    })

# Course detail view
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)  # Retrieve the specific course by ID
    return render(request, 'components/course_detail.html', {
        'course': course,
    })

# Add to cart view
def add_to_cart(request, course_id):
    cart = request.session.get('cart', [])  # Retrieve the cart from the session
    if course_id not in cart:
        cart.append(course_id)  # Add the course ID to the cart
    request.session['cart'] = cart  # Save the updated cart back to the session
    return redirect('cart')  # Redirect to the cart page


# Cart view
def cart(request):
    cart = request.session.get('cart', [])  # Retrieve the cart from the session
    courses = Course.objects.filter(id__in=cart)  # Fetch courses based on the IDs in the cart
    return render(request, 'cart.html', {'courses': courses})  # Pass courses to the cart template


def register(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pw1 = request.POST.get('password1')
        pw2 = request.POST.get('password2')  # Corrected to match 'password2' from the form

        # Basic validations
        if not uname or not email or not pw1 or not pw2:
            messages.error(request, "All fields are required.")
            return render(request, 'components/register.html')

        if pw1 != pw2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'components/register.html')

        # Check if the username already exists
        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username already taken.")
            return render(request, 'components/register.html')

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'components/register.html')

        # Create the user
        try:
            my_user = User.objects.create_user(username=uname, email=email, password=pw1)
            my_user.save()
            messages.success(request, "Account created successfully. You can now log in.")
            return redirect('login')  # Replace 'login' with the name of your login URL
        except Exception as e:
            messages.error(request, "An error occurred while creating the account.")
            return render(request, 'components/register.html')

    return render(request, 'components/register.html')

def LOGIN(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        passw = request.POST.get("password")
        user = authenticate(request, username=uname, password=passw)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or password is incorrect!")

    return render(request, 'components/login.html')


def LOGOUT(request):
    logout(request)
    return redirect("index")