from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    user_type =(
        ("1", "Patient"),
        ("2", "Doctor"),
        ("3", "Insurance Provider"),
    )
    email = forms.EmailField()
    type = forms.ChoiceField(choices = user_type)

    class Meta:
        model = User
        fields = ["username","email","type","password1","password2"]