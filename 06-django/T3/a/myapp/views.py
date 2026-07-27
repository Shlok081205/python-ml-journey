from django.shortcuts import render,HttpResponse


# Create your views here.
def intro(request):
  return render(request,'index.html')

def eng(request):
  return HttpResponse("Bye")

def jap(request):
  return HttpResponse('Saiyonara')

def insert_data(request):
  data ={'name':"Shlok","age":21}
  return render(request,'1.html',{'iData':data})

def list_v(request):
  # Check your views.py structure:
  context = {
      'marks': {'Marks': [{'subject': 'Mathematics', 'score': 95},
      {'subject': 'Science', 'score': 88},{'subject': 'English', 'score': 91},]}}

  return render(request,'2.html',context)