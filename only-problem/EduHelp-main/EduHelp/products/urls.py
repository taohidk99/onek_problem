from django.urls import path
from . import views  
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('add/', views.add_course, name='add_course'),  
    path('update/<int:course_id>/', views.update_course, name='update_course'),  
    path('delete/<int:course_id>/', views.delete_course, name='delete_course'),
     path('add-to-cart/<int:course_id>/', views.add_to_cart, name='add_to_cart'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'), 
     
]