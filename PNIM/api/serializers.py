from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task, Patients

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Patients
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)

        if user_serializer.is_valid():
            user = user_serializer.save()
            patient = Patients.objects.create(user=user, **validated_data)
            return patient

        return user_serializer.errors
    
class PatientUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = ['fname', 'lname', 'age', 'gender', 'address', 'email', 'phone']

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance