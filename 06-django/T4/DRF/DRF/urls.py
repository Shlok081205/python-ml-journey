# core/urls.py
from django.contrib import admin
from django.urls import path, include
from api.views import MyTokenObtainPairView, MyTokenRefreshView # Import custom views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Swapped default views with our customized JWT views
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
    
    path('api/', include('api.urls')),
]