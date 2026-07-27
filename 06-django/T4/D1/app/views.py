from django.shortcuts import render, redirect, get_object_or_404
from .models import Database

def display_data(request):
    all_data = Database.objects.all()
    
    context = {
        'data': all_data
    }
    
    return render(request, 'display.html', context)

def edit_data(request, id):
  item = get_object_or_404(Database, id=id)   
  
  if request.method == "POST":
    item.enr = request.POST.get('enr')
    item.cl = request.POST.get('cl')
    item.name = request.POST.get('name')
        
    item.save() 
    return redirect('display_data') 

  context = {'item': item}
  return render(request, 'edit.html', context)

def add_data(request):
    if request.method == "POST":
        enr = request.POST.get('enr')
        cl = request.POST.get('cl')
        name = request.POST.get('name')
        
        Database.objects.create(enr=enr, cl=cl, name=name)
        
        return redirect('display_data')

    return render(request, 'add.html')

def home_view(request):
  return render(request, 'home.html')


def delete_data(request, id):
    item = get_object_or_404(Database, id=id)
    item.delete()
    
    return redirect('display_data')

