from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

types =(
    ("1", "Patient"),
    ("2", "Doctor"),
    ("3", "Insurance"),
)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    user_type = forms.ChoiceField(choices = types, required=True)
    class Meta:
        model = User
        fields = ["username","email","user_type","password1","password2"]
        