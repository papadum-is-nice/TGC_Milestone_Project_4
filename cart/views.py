from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from guitars.models import Guitars

def add_to_cart(request, guitar_id):
    # attempt to get existing cart from the session using the key "shopping_cart"
    # the second argument will be the default value if 
    # if the key does not exist in the session
    cart = request.session.get('shopping_cart', {})
    
    # we check if the course_id is not in the cart. If so, we will add it
    if guitar_id not in cart:
        guitar = get_object_or_404(Guitars, pk=guitar_id)
        # course is found, let's add it to the cart
        cart[guitar_id] = {
            'id':guitar_id,
            'brand': guitar.brand,
            'cost': str(guitar.cost),
            'quantity':1,
            'image_url':guitar.image.cdn_url,
            # 'subtotal':float(guitar.cost)
        }
        
        # save the cart back to sessions
        request.session['shopping_cart'] = cart
        messages.success(request, "Guitar has been added to your cart!")
    else:
        cart['guitar_id']['cost'] = int(cart[guitar_id]['quantity']) * int(cart[guitar_id]['cost'])
        messages.success(request, "The guitar is already in your shopping cart")
    return redirect('/show_guitars/')
        

def view_cart(request):
    # retrieve the cart
    cart = request.session.get('shopping_cart', {})
    total_price = 0.00
    
    for guitar_id,guitar in cart.items():
        total_price += int(guitar['quantity']) * int(float(guitar['cost']))
    print(total_price)
    
    return render(request, 'view_cart.html', {
        'shopping_cart':cart,
        'total_price':total_price
    })

# def total_price(request, guitar_id):
#     guitar = get_object_or_404(Guitars, pk=guitar_id)
#     cart = request.session.get('shopping_cart', {})
#     cart[guitar_id] = {
#     # 'id':guitar_id,
#     # 'name': game.name,
#     # 'price': str(game.price),
#     # 'image_url':game.image.cdn_url,
#     'quantity':cart['quantity'],
#     'total_price':int(cart[guitar_id]['quantity']) * float(cart[guitar_id]['price'])
#     }
    
#     # print(quantity)
#     request.session['shopping_cart'] = cart
#     return render(request, 'view_cart.html', {
#             'total_price':total_price
#         }) 
        
def remove_from_cart(request, guitar_id):
    cart = request.session.get('shopping_cart', {})
    
    if guitar_id in cart:
        del cart[guitar_id]
        request.session['shopping_cart'] = cart
        messages.success(request, 'Guitar has been removed')
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