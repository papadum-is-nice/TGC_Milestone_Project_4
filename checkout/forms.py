from .models import Charge
from django import forms
from django_countries.fields import CountryField

class OrderForm(forms.ModelForm):
    class Meta:
        model = Charge
        fields = (
            'full_name', 'street_address1', 'street_address2', 'town_or_city', 'postcode', 'country'
            )