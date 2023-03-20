from django.urls import path
from . import views
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path("", views.apiOverview, name="api-overview"),
    path("task-list/", views.taskList, name="task-list"),
    path("task-detail/<str:pk>/", views.taskDetail, name="task-detail"),
    path("task-create/", views.taskCreate, name="task-create"),
    path("task-update/<str:pk>", views.taskUpdate, name="task-update"),
    path("task-delete/<str:pk>", views.taskDelete, name="task-delete"),

    path("patient-create/", views.patient_create, name="patient-create"),
    path("patient-detail/<str:username>/", views.patient_detail, name="patient-detail"),
    path("patient-update/<str:username>", views.patient_update, name="patient-update"),
    path("login", views.login, name="login"),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
