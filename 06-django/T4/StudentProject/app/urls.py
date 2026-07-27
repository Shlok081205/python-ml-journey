from django.urls import path
from . import views

urlpatterns = [
    path('directory/', views.show_directory, name='show_directory'),
]