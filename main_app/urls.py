from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='base'),
  path('about/', views.about, name='about'),
  path('coins/', views.coins_index, name='index'),
  path('coins/<int:coin_id>/', views.coins_detail, name='detail'),
  path('coins/create/', views.CoinCreate.as_view(), name='coins_create'),
  path('coins/<int:pk>/update/', views.CoinUpdate.as_view(), name='coins_update'),
  path('coins/<int:pk>/delete/', views.CoinDelete.as_view(), name='coins_delete'),
  path('coins/<int:coin_id>/add_collecting/', views.add_collecting, name='add_collecting'),
  path('coins/<int:coin_id>/assoc_tool/<int:tool_id>/', views.assoc_tool, name='assoc_tool'),
  path('coins/<int:coin_id>/unassoc_tool/<int:tool_id>/', views.unassoc_tool, name='unassoc_tool'),
  path('tools/', views.ToolList.as_view(), name='tools_index'),
  path('tools/<int:pk>/', views.ToolDetail.as_view(), name='tools_detail'),
  path('tools/create/', views.ToolCreate.as_view(), name='tools_create'),
  path('tools/<int:pk>/update/', views.ToolUpdate.as_view(), name='tools_update'),
  path('tools/<int:pk>/delete/', views.ToolDelete.as_view(), name='tools_delete'),

]