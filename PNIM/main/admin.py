from django.contrib import admin
from .models import Doctor, Patient, InsuranceProvider,Doctor_rating,Insurance_plans,Availability,Patient_History ,Schedule_app

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(InsuranceProvider)
admin.site.register(Doctor_rating)
admin.site.register(Insurance_plans)
admin.site.register(Availability)
admin.site.register(Patient_History)
admin.site.register(Schedule_app)