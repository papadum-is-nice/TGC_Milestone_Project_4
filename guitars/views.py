from django.shortcuts import render, redirect, reverse
from .models import Guitars
from .forms import Guitarsform

# Create your views here.


def show_guitars(request):
    all_guitars = Guitars.objects.all()
    return render(request, 'show_guitars.html', {
        'all_guitars':all_guitars
    })

def create_guitars(request):
    if request.method == 'POST':
        create_guitars_form = Guitarsform(request.POST)
        if create_guitars_form.is_valid():
            create_guitars_form.save()
            return redirect(reverse(show_guitars))
      
    else:
        create_guitars_form = Guitarsform()
  
    return render(request, 'create_guitar.template.html', {
        'form':create_guitars_form
    })