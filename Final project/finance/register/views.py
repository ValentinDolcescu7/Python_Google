from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.http import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def register_request(request):
    """Register user"""

    # User reached route via POST
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect("/")    
        else:
            messages.error(
                request, "Unsuccessful registration!")

    # User reached route via GET
    else:
        form = RegisterForm()

    return render(request=request, template_name="registration/register.html", context={"form": form})


def login_request(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(
                    request, f"Logged in!")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password!")
        else:
            messages.error(request, "Invalid username or password!")

    else:
        form = LoginForm()

    return render(request=request, template_name="registration/login.html", context={"form": form})
