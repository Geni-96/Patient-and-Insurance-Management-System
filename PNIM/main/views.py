from django.shortcuts import render,  redirect
from .forms import RegisterForm
# Create your views here.

def index(response):
    print("reach view folder")
    return render(response, "main/base.html",{})

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:    
        form = RegisterForm()
    return render(response, "main/register.html",{"form":form})

# def login(response):
#     return render(response, "registration/login.html",{})
