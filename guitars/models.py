from django.db import models
# from pyuploadcare.dj.models import ImageField

# Create your models here.

class Guitars(models.Model):
    brand = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)
    prod_year= models.IntegerField(blank=False)
    stockrem= models.IntegerField(blank=False, default=0)
    cost = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    gtype = models.ForeignKey('Gtype', blank=True, null=True, on_delete=models.CASCADE)
    # image = ImageField(blank=True, null=True),
    
    def __str__(self):
        return self.brand + " + " + self.stockrem
    
class Gtype(models.Model):
    name = models.CharField(blank=False, max_length=100)
    
    def __str__(self):
        return self.name

