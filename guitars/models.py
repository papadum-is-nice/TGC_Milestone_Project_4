from django.db import models
from pyuploadcare.dj.models import ImageField

class Guitars(models.Model):
    brand = models.CharField(blank=False, max_length=30)
    model = models.CharField(blank=False, max_length=50)
    gtype = models.ForeignKey('Gtype', blank=True, null=True, on_delete=models.CASCADE)
    desc = models.TextField(blank=False)
    color = models.CharField(blank=False, max_length=50)
    prod_year = models.CharField(blank=True, max_length=4)
    cost = models.FloatField(blank=False)
    stockrem = models.IntegerField(blank=False, default=0)
    image = ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.brand + " " + str(self.model) + " + " + str(self.stockrem)
    
class Gtype(models.Model):
    name = models.CharField(blank=False, max_length=100)
    
    def __str__(self):
        return self.name

