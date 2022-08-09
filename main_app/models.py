from django.db import models
from django.urls import reverse

# Create your models here.

class Coin(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    value = models.IntegerField()
#todo run migrations from

def __str__(self):
    return self.name

def get_absolute_url(self):
    return reverse('detail', kwargs={'coin_id': self.id})