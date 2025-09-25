from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clients/', views.clients, name='clients'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),   
    path('contact/', views.contact, name='contact'),    
    path('signup/',views.signup, name='signup'), 
    path('login/',views.login,  name='login'),
    path('dashboard/',views.dashboard,  name='login'),
]