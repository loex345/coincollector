from multiprocessing import Value
from django.shortcuts import render
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports


# Create your views here.
def about(request):
    return render(request, 'about.html')

def home(request):
  return render(request,'home.html')

def coins_index(request):
   return render(request, 'coins/index.html',{'coins': coins})