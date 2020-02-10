from django import forms
from .models import Guitars
from pyuploadcare.dj.forms import ImageField, FileWidget

class Guitarsform(forms.ModelForm):
    image = ImageField(widget=FileWidget(attrs={'data-clearable':True}))
    class Meta:
        model=Guitars
        fields=('brand', 'desc', 'prod_year', 'stockrem', 'cost', 'gtype', 'image')


class GuitarsSearchForm(forms.Form):
    search_terms = forms.CharField(required=False)
    min_cost = forms.FloatField(required=False,min_value=0.0)
    max_cost = forms.FloatField(required=False)

