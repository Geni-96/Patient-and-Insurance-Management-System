from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer, PatientSerializer, PatientUpdateSerializer
from .models import Task, Patients
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['username'] = self.user.username
        # Add any additional data you want to include in the response
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'login' : '/login/',
        'patient_detail' : '/patient-detail/<str:username>/',
        'patient_create' : '/patient-create/',
        'patient_update': '/patient-update/<str:username>/',
        'Delete': '/task-delete/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['POST'])
def login(request):
    serializer = MyTokenObtainPairSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def patient_create(request):
    serialzer = PatientSerializer(data=request.data)

    if serialzer.is_valid():
        serialzer.save()
        return Response(serialzer.data, status=201)

    return Response(serialzer.data, status=400)

@api_view(['GET'])
def patient_detail(request, username):
    try:
        user = User.objects.get(username=username)
        patient = Patients.objects.get(user=user)
    except (User.DoesNotExist, Patients.DoesNotExist):
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PatientSerializer(patient)
    return Response(serializer.data)

@api_view(['PUT'])
def patient_update(request, username):
    try:
        user = User.objects.get(username=username)
        patient = Patients.objects.get(user=user)
    except (User.DoesNotExist, Patients.DoesNotExist):
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PatientUpdateSerializer(patient, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# EXAMPLES
@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serialzer = TaskSerializer(tasks, many=True)
    return Response(serialzer.data)


@api_view(['GET'])
def taskDetail(request,pk):
    tasks = Task.objects.get(id=pk)
    serialzer = TaskSerializer(tasks, many=False)
    return Response(serialzer.data)


@api_view(['POST'])
def taskCreate(request):
    serialzer = TaskSerializer(data=request.data)

    if serialzer.is_valid():
        serialzer.save()

    return Response(serialzer.data)


@api_view(['POST'])
def taskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    serialzer = TaskSerializer(instance=task, data=request.data)

    if serialzer.is_valid():
        serialzer.save()

    return Response(serialzer.data)


@api_view(['DELETE'])
def taskDelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()    

    return Response(f'Item {task} successfully deleted')