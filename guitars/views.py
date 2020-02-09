from django.shortcuts import render
from .models import Guitars

# Create your views here.


def show_guitars(request):
    all_guitars = Guitars.objects.all()
    return render(request, 'show_guitars.html', {
        'all_guitars':all_guitars
    })

