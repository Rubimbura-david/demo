from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.cache import never_cache
from .models import CustomUser  # Import your CustomUser

@never_cache
def signup(request):
    if request.user.is_authenticated:
        return redirect("home")  # Redirect if already logged in

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, "signup.html")

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

@never_cache
def login(request):
    if request.user.is_authenticated:
        return redirect("home")  # Redirect if already logged in

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials")
            return render(request, "login.html")
    
    return render(request, "login.html")

@login_required
def home(request):
    return render(request, 'index.html')

@login_required
def clients(request):
    return render(request, 'clients.html')

@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def services(request):
    return render(request, 'services.html')

@login_required
def contact(request):
    return render(request, 'contact.html')

def logout(request):
    auth_logout(request)
    messages.info(request, "You have been logged out.")  # Optional message
    return redirect("login")  # Redirect to the login page after logout

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')