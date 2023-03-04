from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.


class Patient(AbstractUser):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    # date_of_birth = models.DateField(default='2022-01-01')
    insurance_id = models.CharField(max_length=100, default='Unknown')
    address = models.CharField(max_length=100, default='Unknown')
    groups = models.ManyToManyField(Group, related_name='patients')
    user_permissions = models.ManyToManyField(
        Permission, related_name='patients')

    class Meta:
        verbose_name_plural = 'Patient'


class Doctor(AbstractUser):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    hospital = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    address = models.CharField(max_length=100, default='Unknown')
    groups = models.ManyToManyField(Group, related_name='doctors')
    user_permissions = models.ManyToManyField(
        Permission, related_name='doctors')

    class Meta:
        verbose_name_plural = 'Doctor'


class InsuranceProvider(AbstractUser):
    name = models.CharField(max_length=100, default='Unknown')
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=100, default='Unknown')
    groups = models.ManyToManyField(Group, related_name='insuranceproviders')
    user_permissions = models.ManyToManyField(
        Permission, related_name='insuranceproviders')

    class Meta:
        verbose_name_plural = 'InsuranceProvider'
