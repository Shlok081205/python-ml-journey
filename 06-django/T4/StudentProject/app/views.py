from django.shortcuts import render
from .models import Student, Dep  # Import both models

def show_directory(request):
    all_students = Student.objects.all()
    all_departments = Dep.objects.all()
    
    context = {
        'students': all_students,
        'departments': all_departments
    }
    return render(request, 'show.html', context)