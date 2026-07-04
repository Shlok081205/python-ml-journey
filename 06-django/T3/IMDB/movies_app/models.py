from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=3, decimal_places=1) # E.g., 8.5, 10.0

    def __str__(self):
        return f"{self.name} ({self.rating}/10)"