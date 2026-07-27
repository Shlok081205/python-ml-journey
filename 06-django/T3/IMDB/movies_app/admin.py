from django.contrib import admin
from .models import Movie # Import your model

# Tell Django to show this model in the admin panel
admin.site.register(Movie)