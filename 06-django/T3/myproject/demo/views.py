from django.shortcuts import render,HttpResponse


# Create your views here.
def intro(request):
  return HttpResponse("Hello World")

def eng(request):
  return HttpResponse("Bye")

def jap(request):
  return HttpResponse('Saiyonara')

def landing(request):
  return render(request,"synthwave.html")