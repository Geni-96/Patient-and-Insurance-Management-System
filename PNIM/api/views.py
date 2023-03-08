from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/task-list/',
        'Detail View' : '/task-detail/<str:pk>/',
        'Create' : '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/'
    }
    return Response(api_urls)


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