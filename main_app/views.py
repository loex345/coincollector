from multiprocessing import Value
from django.shortcuts import render
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Coin:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, type, description, value):
    self.name = name
    self.type = type
    self.description = description
    self.value = value

coins = [
  Coin('Peace Dollar', 'silver', 'peace dollar', 1),
  Coin('Lincoln Cent', 'bronze', 'Lincoln coin', .01),
]


# Create your views here.
def about(request):
    return render(request, 'about.html')

def home(request):
  return render(request,'home.html')

def coins_index(request):
   return render(request, 'coins/index.html',{'coins': coins})