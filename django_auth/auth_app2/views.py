from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import details

# Create your views here.
def register(request):
    if request.method == "POST":
        user = request.POST["name"]
        password = request.POST["password"]
        print(user)
        print(password)
        if User.objects.filter(username=user).exists():
            messages.error(request, "Username already exists !!")
        else:
            user = User.objects.create_user(user,password)
            login(request,user)
            return redirect("dashboard")
    return render(request, "auth_app2/register.html")


@login_required(login_url="login")
def dashboard(request):
    return render(request,"auth_app2/dashboard.html")


def login_view(request):
    if request.method == "POST":
        user = request.POST["user"]
        password = request.POST["password"]      
        final = authenticate(request,username=user,password=password)
        if final is not None:
            login(request, final)
            return redirect("dashboard")
        else:
            messages.error(request,"invalid credentials")
    return render(request, "auth_app2/login.html",{"error_message": "You didn't select a choice."})

def logout_view(request):
    logout(request)
    return redirect("login")



# crud operations

def create(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        test = details.objects.create(name=name,email=email,number=mobile)
        test.save()
        return redirect("home")
    return render(request,"auth_app2_crud/create.html")