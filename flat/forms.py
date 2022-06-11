from django import forms
from . import models

class FlatForm(forms.ModelForm):
    class Meta:
        model = models.Flat
        fields = '__all__'

