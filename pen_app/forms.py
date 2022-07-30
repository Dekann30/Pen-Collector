from dataclasses import field
from django.forms import ModelForm
from .models import Pen

class PenForm(ModelForm):
    class Meta:
        model = Pen
        fields = ['brand', 'color', 'number_owned']