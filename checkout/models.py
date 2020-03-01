from django.db import models
from django_countries.fields import CountryField

class Charge(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    country = CountryField(multiple=False)

    def __str__(self):
        return "{0}-{1}".format(self.id, self.full_name)