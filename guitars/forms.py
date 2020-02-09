from django import forms
from .models import Guitars
from pyuploadcare.dj.forms import ImageField, FileWidget

class Guitarsform(forms.ModelForm):
    image = ImageField(widget=FileWidget(attrs={'data-clearable':True}))
    class Meta:
        model=Guitars
        fields=('brand', 'desc', 'prod_year', 'stockrem', 'cost', 'gtype', 'image')
