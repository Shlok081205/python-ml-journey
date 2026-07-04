from django.urls import path
from app import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('data/', views.display_data, name='display_data'),
    path('add/', views.add_data, name='add_data'),
    path('edit/<int:id>/', views.edit_data, name='edit_data'), 
    path('delete/<int:id>/', views.delete_data, name='delete_data'), 
]