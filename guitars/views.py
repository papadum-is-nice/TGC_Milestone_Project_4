from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Guitars
from .forms import Guitarsform, GuitarsSearchForm

def show_guitars(request):
    all_guitars = Guitars.objects.all()
    # form = GuitarsSearchForm()
    if request.GET.get('search_terms'):
        all_guitars = all_guitars.filter(Q(brand__icontains=request.GET.get('search_terms'))|Q(model__icontains=request.GET.get('search_terms'))|Q(gtype__name__icontains=request.GET.get('search_terms'))|Q(desc__icontains=request.GET.get('search_terms')))
    # if request.GET.get('min_cost'):
    #     all_guitars = all_guitars.filter(cost__gte=request.GET.get('min_cost'))
    # if request.GET.get('max_cost'):
    #     all_guitars = all_guitars.filter(cost__lte=request.GET.get('max_cost'))
    return render(request, 'show_guitars.html', {
        'all_guitars':all_guitars,
        # 'search_form':form,
    })
    
# def guitar_info(request):
#     all_guitars = Guitars.objects.all()
#     return render(request, 'guitar_info.html', {
#         'all_guitars':all_guitars,
#     })    

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
        update_guitars_form = Guitarsform(request.POST, instance=guitars_being_updated)
        if update_guitars_form.is_valid():
            update_guitars_form.save()
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