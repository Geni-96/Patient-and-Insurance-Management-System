from django.shortcuts import render, redirect
from .forms import RegistrationForm, PatientRegistrationForm, InsuranceProviderRegistrationForm, DoctorRegistrationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage
from django.contrib.auth import get_user_model
from .models import Patient, Doctor, InsuranceProvider
import os

# from .send_email import send_email
# Create your views here.
def landingtemp(response):
    return render(response, "main/basenew.html", {})


def send_email(target, message_type='registration'):
    load_dotenv('pwds.env')
    u_id = 'careconnectiub@gmail.com'
    pwd = 'pvofhbltndpitopa'
    # pwd = os.environ.get('EMAIL_PASSWORD')
    print(pwd)
    if message_type == 'registration':
        message = 'Thank you for registering with CareConnect. We will get back to you soon.'
    elif message_type == 'appointment':
        message = 'Your appointment has been confirmed. Please visit the hospital on the given date and time.'
    else:
        message = 'Your request has been received. We will get back to you soon.'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(u_id, pwd)
    msg = EmailMessage()

    html_mesage = f"""\
    <html>
        <body>
            <h1>CareConnect</h1>
            <p>{message}</p>
        </body>
    </html>
    """

    msg['Subject'] = 'CareConnect Alerts'
    msg['From'] = 'CareConnect'
    msg['Name'] = 'CareConnect'
    msg['To'] = target
    # msg.set_content(message)
    msg.add_alternative(html_mesage, subtype='html')
    server.send_message(msg)
    server.quit()


def landing(response):
    return render(response, "main/landing.html", {})


@login_required(login_url="/login")
def home(response):
    # redirect to react app
    # return
    results = []
    # get all doctors from database
    doctors = Doctor.objects.all()
    # doctors = Patient.objects.all()
    print(doctors)
    # for doctor in doctor
    results.append(doctors)
    # return render(response, "http://localhost:3000/", {})
    return render(response, "main/home.html", {'results': list(doctors),'user': response.user})


# def signup(response):
#     if response.POST:
#         print(response.POST)
#         form = RegistrationForm(response.POST)
#         print(form)
#         if form.is_valid():
#             user = form.save()
#             # get user email from the form
#             user_email = form.cleaned_data.get('email')
#             username = form.cleaned_data.get('username')
#             user_type = form.cleaned_data.get('user_type')
#             send_email(user_email, 'registration')
#             # user = form.save()
#             login(response, user)
#             return redirect("/home", {'username': username, 'user_type': user_type})
#     else:
#         form = RegistrationForm()
#     return render(response, "registration/signup.html", {"form": form})

@login_required(login_url="/login")
def profile_page(response):
    user_details = response.user
    # get patients with the same username
    try:
        patient = Patient.objects.filter(username=user_details)
    except Patient.DoesNotExist:
        patient = None
    try:
        doctor = Doctor.objects.filter(username=user_details)
    except Doctor.DoesNotExist:
        doctor = None
    try:
        insurance = InsuranceProvider.objects.filter(username=user_details)
    except InsuranceProvider.DoesNotExist:
        insurance = None
    if patient:
        user_details = patient
        print('patient', patient)
    elif doctor:
        user_details = doctor
        print('doctor', doctor)
    elif insurance:
        user_details = insurance
        print('insurance', insurance)
    return render(response, "main/profile.html", {'user_details': user_details})


def signup(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        if user_type == 'patient':
            form = PatientRegistrationForm(request.POST)
        elif user_type == 'doctor':
            form = DoctorRegistrationForm(request.POST)
        elif user_type == 'insurance_provider':
            form = InsuranceProviderRegistrationForm(request.POST)
        else:
            form = None

        if form and form.is_valid():
            user = form.save(commit=False)
            user.user_type = user_type
            user.save()
            user_email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            send_email(user_email, 'registration')
            # save Patient, Doctor or InsuranceProvider
            # if user_type == 'patient':
            #     patient = form.save_patient()
            #     patient.user = user
            #     patient.save()
            # elif user_type == 'doctor':
            #     doctor = form.save_doctor()
            #     doctor.user = user
            #     doctor.save()
            # elif user_type == 'insurance_provider':
            #     insurance_provider = form.save_insurance_provider()
            #     insurance_provider.user = user
            #     insurance_provider.save()

            User = get_user_model()
            user_data = {
                'username': user.username,
                'password': user.password,
                'email': user.email,
            }
            User.objects.create_user(**user_data)
            # auth_user = authenticate(username=user.username, password=request.POST['password1'])
            # login(request, auth_user)
            return redirect('home')
        # return render(request, 'home.html', {'form': form})

    else:
        form = None
    return render(request, 'registration/signup.html', {'form': form})
