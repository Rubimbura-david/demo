from django.shortcuts import render

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
def signup(request):    
    return render(request, 'signup.html')

def login(request):    
    return render(request, 'login.html')

def dashboard(request):    
    return render(request, 'dashboard.html')