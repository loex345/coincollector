from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='base'),
  path('about/', views.about, name='about'),
  path('coins/', views.coins_index, name='index'),
]