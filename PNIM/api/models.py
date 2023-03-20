from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=30)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title
    
# {
#     "fname": "John",
#     "lname": "Doe",
#     "age": 30,
#     "gender": "M",
#     "address": "123 Main St",
#     "email": "johndoe@example.com",
#     "phone": "556-1234",
#     "user": {
#         "username": "johndoe",
#         "email": "johndoe@example.com",
#         "password": "mypassword"
#     }
# }

# {
#     "fname": "John",
#     "lname": "Doe",
#     "age": 31,
#     "gender": "M",
#     "address": "456 New St",
#     "email": "johndoe@example.com",
#     "phone": "556-1234",
#     "user": {
#         "username": "johndoe",
#         "email": "johndoe@example.com",
#         "password": "mypassword"
#     }
# }

class Patients(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    user=models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    age=models.IntegerField()
    Gender=[('M','Male'),('F','Female'),('O','Other')]
    gender=models.CharField(max_length=1,choices=Gender)
    address= models.TextField()
    email=models.EmailField(max_length=30)
    phone=models.CharField(max_length=30)