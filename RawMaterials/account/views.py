from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.http import HttpResponse
from .forms import RegisterForm


def admin_dashboard(request):
    return HttpResponse("Admin Dashboard")

def customer_home(request):
    return HttpResponse("Customer Home")

def contractor_dashboard(request):
    return HttpResponse("Contractor Dashboard")

def register(request):
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.role == 'admin':
                return redirect('admin_dashboard')
            elif user.role == 'contractor':
                return redirect('contractor_dashboard')
            else:
                return redirect('customer_home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
        
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('user_login')


