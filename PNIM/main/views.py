from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage
import os

# from .send_email import send_email
# Create your views here.


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

    # return render(response, "http://localhost:3000/", {})
    return render(response, "main/home.html", {})


def signup(response):
    if response.POST:
        print(response.POST)
        form = RegistrationForm(response.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            # get user email from the form
            user_email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            user_type = form.cleaned_data.get('user_type')
            send_email(user_email, 'registration')
            # user = form.save()
            login(response, user)
            return redirect("/home", {'username': username, 'user_type': user_type})
    else:
        form = RegistrationForm()
    return render(response, "registration/signup.html", {"form": form})
