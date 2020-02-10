from django.shortcuts import render, reverse, HttpResponse, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

#import settings so that we can access the public stripe key
from django.conf import settings
import stripe

from guitars.models import Guitars

from django.views.decorators.csrf import csrf_exempt

endpoint_secret = "whsec_hEvKOilMog4Q4oPdUlmk7kUdrmPz42DH"

# Create your views here.
def checkout(request):
    # print(settings.STRIPE_SECRET_KEY)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    # retrieve shopping cart
    cart = request.session.get('shopping_cart', {})
    
    line_items = []
    
    # generate the line_items
    for id,guitars in cart.items():
        # For each item in the cart, get its details from the database
        guitars = get_object_or_404(Guitars, pk=id)
        line_items.append({
            'name': guitars.brand,
            'amount': int(guitars.cost*100), #convert to cents, in integer
            'currency':'sgd',
            'quantity':1
        })
    
    #generate the session
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        success_url=request.build_absolute_uri(reverse('home')),
        cancel_url=request.build_absolute_uri(reverse('home')),
        payment_intent_data={
            'capture_method':'manual'
        }
        
    )
    
    # render the template
    return render(request, 'checkout.html', {
        'session_id':session.id,
        'public_key': settings.STRIPE_PUBLISHABLE_KEY
    })
    
def checkout_success(request):
    # Empty the shopping cart
    request.session['shopping_cart'] = {}
    return HttpResponse("Checkout success")
    
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
    # Invalid payload
    return HttpResponse(status=400)
  except stripe.error.SignatureVerificationError as e:
    # Invalid signature
    return HttpResponse(status=400)

  # Handle the checkout.session.completed event
  if event['type'] == 'checkout.session.completed':
    session = event['data']['object']

    # Fulfill the purchase...
    handle_checkout_session(session)

  return HttpResponse(status=200)
  
def handle_checkout_session(session):
     print(session)
     
     