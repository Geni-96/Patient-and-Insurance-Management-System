from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/login")
def home(response):
    return render(response, "main/home.html", {})

def signup(response):
    if response.POST:
        form = RegistrationForm(response.POST)
        if form.is_valid():
            user = form.save()
            login(response,user)
            return redirect("/home")
    else:
        form = RegistrationForm()
    return render(response, "registration/signup.html",{"form":form})