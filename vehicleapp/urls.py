from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clients/', views.clients, name='clients'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),   
    path('contact/', views.contact, name='contact'),    
<<<<<<< HEAD
    path('signup/',views.signup, name='signup'), 
    path('login/',views.login,  name='login'),
    path('dashboard/',views.dashboard,  name='login'),
=======
    path('signup/', views.signup, name='signup'), 
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),  # Add this line
>>>>>>> 2d2af42da0903be56fd271bf2974bd36a01301b8
]