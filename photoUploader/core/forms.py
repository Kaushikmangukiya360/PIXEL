from django import forms
from .models import *

class imgForm(forms.ModelForm):
    class Meta:
        model = imgData
        fields = '__all__'
        labels = {'img': ''}