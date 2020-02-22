"""jimbos_guitarshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import home
from users.views import signup, profile
from guitars.views import show_guitars, create_guitars, update_guitars, confirm_delete_guitar, actually_delete_guitar
from cart.views import add_to_cart, view_cart, remove_from_cart, adjust_cart
from checkout.views import checkout, checkout_success, checkout_cancelled, payment_completed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('show_guitars/', show_guitars, name="show_guitars"),
    path('create_guitars/', create_guitars),
    path('update_guitars/<guitar_id>', update_guitars, name="update_guitar"),
    path('confirm_delete_guitar/<guitar_id>', confirm_delete_guitar, name="confirm_delete_guitar"),
    path('actually_delete/<guitar_id>', actually_delete_guitar, name='delete_guitar'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    # path('login/', login),
    # path('logout/', logout),
    # path('signup/', signup),
    path('profile/', profile),
    path('cart/', view_cart, name="view_cart"),
    path('add_to_cart/<guitar_id>', add_to_cart, name="add_to_cart"),
    path('adjust_cart/<guitar_id>', adjust_cart, name='adjust_cart'),
    path('remove/<guitar_id>', remove_from_cart, name="remove_from_cart"),
    path('checkout/', checkout, name='checkout'),
    path('success/', checkout_success),
    path('cancelled/', checkout_cancelled),
    path('payment_completed/', payment_completed),
    
]

