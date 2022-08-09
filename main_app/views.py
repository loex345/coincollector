from multiprocessing import Value
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Coin

# Add the Cat class & list and view function below the imports


# Create your views here.
def about(request):
    return render(request, 'about.html')

def home(request):
  return render(request,'home.html')

def coins_index(request):
   coins = Coin.objects.all()
   return render(request, 'coins/index.html',{'coins': coins})

def coins_detail(request, coin_id):
   coin = Coin.objects.get(id=coin_id)
   return render(request, 'coins/detail.html', {'coin':coin})

class CoinCreate(CreateView):
      model= Coin
      fields ='__all__'

class CoinUpdate(UpdateView):
      model = Coin
      fields = ['name','type','description','value',]

class CoinDelete(DeleteView):
      model = Coin
      success_url = '/cats/'
      

