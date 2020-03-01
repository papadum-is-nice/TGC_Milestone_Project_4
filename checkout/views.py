from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.conf import settings
from guitars.models import Guitars
from .forms import OrderForm
import stripe

endpoint_secret = "whsec_hEvKOilMog4Q4oPdUlmk7kUdrmPz42DH"

@login_required
def place_order(request):
    return render(request, 'place_order.html', {
        'order_form':OrderForm
    })
    
def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('shopping_cart', {})
    
    line_items = []
    
    for id,guitar in cart.items():
        guitars = get_object_or_404(Guitars, pk=id)
        line_items.append({
            'name': guitars.brand,
            'amount': int(guitars.cost*100),
            'currency':'sgd',
            'quantity':guitar['quantity']
        })
    
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        success_url=request.build_absolute_uri(reverse(checkout_success)),
        cancel_url=request.build_absolute_uri(reverse('home')),
        payment_intent_data={
            'capture_method':'manual'
        })
    
    return render(request, 'checkout.html', {
        'session_id':session.id,
        'public_key': settings.STRIPE_PUBLISHABLE_KEY
    })
    
def checkout_success(request):
    request.session['shopping_cart'] = {}
    return redirect('/')
    
def checkout_cancelled(request):
    return HttpResponse("Checkout cancelled")
    
@csrf_exempt
def payment_completed(request):
  payload = request.body
  sig_header = request.META['HTTP_STRIPE_SIGNATURE']
  event = None

  try:
    event = stripe.Webhook.construct_event(
      payload, sig_header, endpoint_secret
    )
  except ValueError as e:
    return HttpResponse(status=400)
  except stripe.error.SignatureVerificationError as e:
    return HttpResponse(status=400)

  if event['type'] == 'checkout.session.completed':
    session = event['data']['object']
    handle_checkout_session(session)
    request.session['shopping_cart'] = {}
  return HttpResponse(status=200)
  
def handle_checkout_session(session):
     print(session)