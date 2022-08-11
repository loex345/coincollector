from ast import Del
from multiprocessing import Value
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Coin, Tool
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
   id_list = coin.tools.all().values_list('id')
   tools_coin_doesnt_have = Tool.objects.exclude(id__in=id_list)
   collecting_form = CollectingForm()
   return render(request, 'coins/detail.html', {'coin':coin, 'collecting_form':collecting_form, 'tools': tools_coin_doesnt_have})

class CoinCreate(CreateView):
      model= Coin
      fields =['name','type','description','value',]
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

class ToolList(ListView):
      model = Tool

class ToolDetail(DetailView):
      model = Tool

class ToolCreate(CreateView):
      model = Tool
      fields ='__all__'

class ToolUpdate(UpdateView):
      model = Tool
      fields ='__all__'

class ToolDelete(DeleteView):
      model = Tool
      success_url ='/tools/'

def assoc_tool(request, coin_id, tool_id):
   Coin.objects.get(id=coin_id).tools.add(tool_id)
   return redirect('detail', coin_id=coin_id)

def unassoc_tool(request, coin_id, tool_id):
   Coin.objects.get(id=coin_id).tools.remove(tool_id)
   return redirect('detail', coin_id=coin_id)