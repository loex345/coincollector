from django.contrib import admin
from .models import Coin, Collecting

# Register your models here.
admin.site.register(Coin)
# new model
admin.site.register(Collecting)
