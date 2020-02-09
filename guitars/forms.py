from django import forms
from .models import Guitars

class Guitarsform(forms.ModelForm):
    class Meta:
        model=Guitars
        fields=('brand', 'desc', 'prod_year', 'stockrem', 'cost', 'gtype')
