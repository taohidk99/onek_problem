from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .forms import CourseForm


def home(request):
    # Fetch the 3 most added courses based on CartItem count
    popular_courses = Course.objects.annotate(cart_count=Count('cartitem')).order_by('-cart_count')[:3]
    all_courses = Course.objects.all()
    return render(request, 'home.html', {
        'popular_courses': popular_courses,
        'all_courses': all_courses,
    })

def index(request):
    return render(request, 'index.html')
# Add a new course
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()  
            return redirect('home')  
    else:
        form = CourseForm()  
    return render(request, 'courseform.html', {'form': form})  

# Update an existing course
def update_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id) 
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)  
        if form.is_valid():
            form.save()  
            return redirect('course') 
    else:
        form = CourseForm(instance=course) 
    return render(request, 'courseform.html', {'form': form})  


def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)  
    course.delete()  
    return redirect('course')

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
        cart.append(course_id)  # Add the course to the cart
    request.session['cart'] = cart  # Save the cart back to the session
    return redirect('cart')  # Redirect to the cart page

# Cart view
def cart(request):
    cart = request.session.get('cart', [])
    courses = Course.objects.filter(id__in=cart)  # Retrieve courses in the cart
    return render(request, 'cart.html', {'courses': courses})



