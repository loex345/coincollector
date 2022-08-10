from django.forms import ModelForm
from .models import Collecting

class CollectingForm(ModelForm):
    class Meta:
        model = Collecting
        fields = ['date', 'duration', 'prospecting'] 