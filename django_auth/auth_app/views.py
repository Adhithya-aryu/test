from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User 
from django.contrib.auth import login, logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == "POST":
        user = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        if User.objects.filter(username=user).exists():
            messages.error(request, "Username already exists")
        else:
            user=User.objects.create_user(user,email,password)
            login(request,user)
            return redirect("dashboard")
    return render(request, "auth_app/register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["name"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("dashboard")
        else:
            messages.error(request,"Invalid credentials")
    return render(request,"auth_app/login.html")

@login_required(login_url="login")          
def dashboard(request):
    return render(request, "auth_app/dashboard.html")

def logout_view(request):
    logout(request)
    return redirect("login")