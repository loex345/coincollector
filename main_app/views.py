from multiprocessing import Value
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Coin
from .forms import CollectingForm

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
   collecting_form = CollectingForm()
   return render(request, 'coins/detail.html', {'coin':coin, 'collecting_form':collecting_form})

class CoinCreate(CreateView):
      model= Coin
      fields ='__all__'
      success_url = '/coins/'

class CoinUpdate(UpdateView):
      model = Coin
      fields = ['name','type','description','value',]

class CoinDelete(DeleteView):
      model = Coin
      success_url = '/coins/'
      
def add_collecting(request, coin_id):
      form = CollectingForm(request.POST)
      if form.is_valid():
          new_collecting = form.save(commit=False)
          new_collecting.coin_id = coin_id
          new_collecting.save()
      return redirect('detail', coin_id=coin_id)    

