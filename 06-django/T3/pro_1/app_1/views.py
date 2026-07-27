from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return render(request, 'home.html')

def base(request):
    return render(request, 'base.html')

def form(request):
  return render(request,'form.html')

def show_data(request):
  name = request.GET.get('name')
  email = request.GET.get('email')
  content ={"name":name,"email":email}
  return render(request,'show_data.html',content)
