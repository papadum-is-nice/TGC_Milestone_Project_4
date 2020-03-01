from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from guitars.models import Guitars

def add_to_cart(request, guitar_id):
    cart = request.session.get('shopping_cart', {})
    if guitar_id not in cart:
        guitar = get_object_or_404(Guitars, pk=guitar_id)
        cart[guitar_id] = {
            'id':guitar_id,
            'brand': guitar.brand,
            'cost': str(guitar.cost),
            'quantity':1,
            'image_url':guitar.image.cdn_url,
        }
        request.session['shopping_cart'] = cart
        messages.success(request, "New item has been added to your cart!")
    else:
        messages.success(request, "Item is already in your shopping cart")
    return redirect('/show_guitars/')
        

def view_cart(request):
    cart = request.session.get('shopping_cart', {})
    total_price = 0.00
    
    for guitar_id,guitar in cart.items():
        total_price += int(guitar['quantity']) * int(float(guitar['cost']))
    
    return render(request, 'view_cart.html', {
        'shopping_cart':cart,
        'total_price':total_price
    })

def remove_from_cart(request, guitar_id):
    cart = request.session.get('shopping_cart', {})
    
    if guitar_id in cart:
        del cart[guitar_id]
        request.session['shopping_cart'] = cart
        messages.success(request, 'Item has been removed')
        return redirect('/cart/') 
        
def adjust_cart(request, guitar_id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('shopping_cart', {})

    if quantity > 0:
        cart[guitar_id]["quantity"]= quantity
    else:
        cart.pop(id)
    
    request.session['shopping_cart'] = cart
    return redirect(reverse('view_cart')) 