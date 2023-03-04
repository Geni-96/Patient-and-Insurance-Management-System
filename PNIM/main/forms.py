from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Patient, Doctor, InsuranceProvider

types = (
    ("1", "Patient"),
    ("2", "Doctor"),
    ("3", "Insurance"),
)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    user_type = forms.ChoiceField(choices=types, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "user_type", "password1", "password2"]


# class PatientRegistrationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = Patient
#         fields = ("username", 'firstname', 'lastname', 'email', 'phone_number',
#                   'date_of_birth', 'insurance_id', 'address', 'password1', 'password2')


class PatientRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Patient
        fields = ("username", 'firstname', 'lastname', 'email', 'phone_number',
                  'insurance_id', 'address', 'password1', 'password2')


class DoctorRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Doctor
        fields = ("username", 'firstname', 'lastname', 'email', 'phone_number',
                  'hospital', 'specialization', 'address', 'password1', 'password2')


class InsuranceProviderRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = InsuranceProvider
        fields = ("username", 'name', 'email', 'phone_number',
                  'address', 'password1', 'password2')
