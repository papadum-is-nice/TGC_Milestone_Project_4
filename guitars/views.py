from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Guitars
from .forms import Guitarsform, GuitarsSearchForm

# Create your views here.


def show_guitars(request):
    all_guitars = Guitars.objects.all()
    # all_models = Guitars.objects.filter(model__contains)
    form = GuitarsSearchForm()
    if request.GET.get('search_terms'):
        all_guitars = all_guitars.filter(Q(brand__contains=request.GET.get('search_terms'))|Q(model__contains=request.GET.get('search_terms'))|Q(gtype__name__contains=request.GET.get('search_terms'))|Q(desc__contains=request.GET.get('search_terms')))
        # all_models = all_guitars.filter(model__contains=request.GET.get('search_terms'))
        # print(all_models)
    if request.GET.get('min_cost'):
        all_guitars = all_guitars.filter(cost__gte=request.GET.get('min_cost'))
    if request.GET.get('max_cost'):
        all_guitars = all_guitars.filter(cost__lte=request.GET.get('max_cost'))
    return render(request, 'show_guitars.html', {
        'all_guitars':all_guitars,
        'search_form':form,
        # 'all_models':all_models
    })

def create_guitars(request):
    if request.method == 'POST':
        create_guitars_form = Guitarsform(request.POST)
        if create_guitars_form.is_valid():
            create_guitars_form.save()
            messages.success(request, "Guitar is newly created!")
            return redirect(reverse(show_guitars))
      
    else:
        create_guitars_form = Guitarsform()
  
    return render(request, 'create_guitar.html', {
        'form':create_guitars_form
    })
    

def update_guitars(request, guitar_id):
    guitars_being_updated = get_object_or_404(Guitars, pk=guitar_id)
    
    if request.method == "POST":
        # for update
        update_guitars_form = Guitarsform(request.POST, instance=guitars_being_updated)
        if update_guitars_form.is_valid():
            update_guitars_form.save()
         
            # always make sure to return the redirect
            return redirect(reverse(show_guitars))
    else:
        update_guitars_form = Guitarsform(instance=guitars_being_updated)
    
    return render(request, 'update_guitars.html',{
        'form':update_guitars_form
    })
    
def confirm_delete_guitar(request, guitar_id):
    guitar_being_deleted = get_object_or_404(Guitars, pk=guitar_id)
    return render(request, 'confirm_delete_guitar.html', {
        'guitar':guitar_being_deleted
    })
    

def actually_delete_guitar(request, guitar_id):
    guitar_being_deleted = get_object_or_404(Guitars, pk=guitar_id)
    guitar_being_deleted.delete()
    return redirect(reverse('show_guitars'))