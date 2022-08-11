from django.db import models
from django.urls import reverse
from datetime import date

PROSPECTING_TIMES =(
    ('M', 'Morning'),
    ('N', 'Noon'),
    ('E', 'Evening'),
)
# Create your models here.

class Tool(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=150)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('tools_detail', kwargs={'pk': self.id})

class Coin(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    value = models.IntegerField()
    tools = models.ManyToManyField(Tool)
#Tools
#todo run migrations from

    def __str__(self):
       return self.name

    def get_absolute_url(self):
       return reverse('detail', kwargs={'coin_id': self.id})

    def prospect_for_today(self):
      return self.collecting_set.filter(date=date.today()).count() >=len(PROSPECTING_TIMES) 

class Collecting(models.Model):
     date = models.DateField('Collection date')
     duration = models.IntegerField()
     prospecting = models.CharField(max_length=1, choices=PROSPECTING_TIMES, default=PROSPECTING_TIMES[0][0])
     coin = models.ForeignKey(Coin, on_delete=models.CASCADE, default=0)
     
     def __str__(self):
        return f'{self.get_prospecting_display()} on {self.date}'
     class Meta:
        ordering =['-date'] 
    