from django.db import models

# Create your models here.
class Dep(models.Model):
    hod_name = models.CharField(max_length=100)
    dept_name = models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField() 
    enroll = models.IntegerField()
    department = models.ForeignKey("Dep", on_delete=models.CASCADE)
  
    def __str__(self):
        return self.name