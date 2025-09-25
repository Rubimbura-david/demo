from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser  # Import your CustomUser

def home(request):
    return render(request, 'index.html')

def clients(request):
    return render(request, 'clients.html')

def about(request):
    return render(request, 'about.html')

def services(request):   
    return render(request, 'services.html')

def contact(request):    
    return render(request, 'contact.html')

<<<<<<< HEAD
def login(request):    
    return render(request, 'login.html')

def dashboard(request):    
=======
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")

        if CustomUser.objects.filter(username=username).exists():
            return render(request, "signup.html", {"error": "Username already exists"})
        
        # Use CustomUser instead of User
        user = CustomUser.objects.create_user(
            username=username, 
            email=email, 
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        auth_login(request, user)
        return redirect("home")
    return render(request, "signup.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")

def logout(request):
    auth_logout(request)
    return redirect("home")

@login_required
def dashboard(request):
>>>>>>> 2d2af42da0903be56fd271bf2974bd36a01301b8
    return render(request, 'dashboard.html')