from django.db import models
from django.urls import reverse

PROSPECTING_TIMES =(
    ('M', 'Morning'),
    ('N', 'Noon'),
    ('E', 'Evening'),
)
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

class Collecting(models.Model):
     date = models.DateField('Collection date')
     duration = models.IntegerField()
     prospecting = models.CharField(max_length=1, choices=PROSPECTING_TIMES, default=PROSPECTING_TIMES[0][0])
     coin = models.ForeignKey(Coin, on_delete=models.CASCADE, default=0)
     def __str__(self):
        return f"{self.get_prospecting_display()} on {self.date}"