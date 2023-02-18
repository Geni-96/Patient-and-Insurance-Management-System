from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def index(response):
    print("reach view folder")
    return render(response, "main/base.html",{})

def register(response):
    form = UserCreationForm()
    return render(response, "main/register.html",{"form":form})

def login(response):
    return render(response, "main/login.html",{})
