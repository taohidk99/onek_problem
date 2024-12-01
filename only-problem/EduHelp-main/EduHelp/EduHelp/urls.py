from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings, views

urlpatterns = [
     path('', views.index, name='index'),  # Landing page
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('base', views.base, name='base'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register, name='register'),
    path('login/', views.LOGIN, name='login'),
    path('logout/', views.LOGOUT, name='logout'),
    path('course/', views.course, name='course'),
    path('products/', include('products.urls')),

    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('add-to-cart/<int:course_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
     path('add-to-cart/<int:course_id>/', views.add_to_cart, name='add_to_cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
