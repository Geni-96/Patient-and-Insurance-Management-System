from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path("",views.home,name="home"),
    path("", views.landing, name="landing"),
    path("home", views.home, name="home"),
    path("signup", views.signup, name="signup"),
    path("profile", views.profile_page, name="profile"),
    path("test", views.landingtemp, name="profile"),
    path("reset_password/", auth_views.PasswordResetView.as_view(template_name="main/password_reset.html"), name="reset_password"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="main/password_reset_sent.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="main/password_reset_form.html"), name = "password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetView.as_view(template_name="main/password_reset_done.html"), name="password_reset_complete"),
]
