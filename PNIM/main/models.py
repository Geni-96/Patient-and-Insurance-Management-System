from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

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

class Insurance_plans(models.Model):
      plan_id =models.BigAutoField(primary_key=True)
      insurance_id=models.ForeignKey(InsuranceProvider,on_delete=models.CASCADE)
      description=models.TextField()
      
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
    age=models.IntegerField(max_length=3,default=0)
    Gender=[('M','Male'),('F','Female'),('O','Other')]
    gender=models.CharField(max_length=1,choices=Gender,default="Unknown")
    #i_id=models.ManyToManyField(InsuranceProvider)
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

class Doctor_rating(models.Model):
    doctor_id=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    comments=models.TextField()
    Rating=[('1','Worst'),('2','Bad'),('3','Average'),('4','Good'),('5','Excellent')]
    ratings=models.IntegerField(choices=Rating,default=0)
    class Meta:
        verbose_name_plural = 'Doctor Ratings'

class Availability(models.Model):
    doctor_id=models.ManyToManyField(Doctor)
    date=models.DateField()
    time=models.TimeField()
    class Meta:
        verbose_name_plural = 'Availability'

class Patient_History(models.Model):
    report_id =models.BigAutoField(primary_key=True)
    patient_id=models.ForeignKey(Patient,on_delete=models.CASCADE)
    description=models.TextField()
    class Meta:
        verbose_name_plural = 'Patient History'

class Schedule_app(models.Model):
    patient_id=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor_id=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Schedule Appointment'
