# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Route to the task_list function
    path('tasks/', views.task_list, name='task-list'),
    
    # Route to the task_detail function (requires an ID in the URL)
    path('tasks/<int:pk>/', views.task_detail, name='task-detail'),
]