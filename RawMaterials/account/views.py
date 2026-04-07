from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout 
# Create your views here.
from django.http import HttpResponse
from .forms import RegisterForm


def admin_dashboard(request):
    return HttpResponse("Admin Dashboard")

def customer_home(request):
    return HttpResponse("Customer Home")

def contractor_dashboard(request):
    return HttpResponse("Contractor Dashboard")
#REGISTER
def register(request):
    form=RegisterForm()
    
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('login')
    
    return render(request,'register.html',{'form':form})
#LOGIN
def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=authenticate(request,username=username,password=password)
        
        if user:
            login(request,user)
            if user.role =='admin':
                return redirect('admin_dashboard')
            elif user.role=='constrator':
                return redirect('contractor_dashboard')
            else:
                return redirect('ustomer_home')
        
    return render(request, 'login.html')

#LOGOUT
def user_logout(request):
    logout(request)
    return redirect('login')


