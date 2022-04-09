from django.shortcuts import render
from django.http import JsonResponse

from .models import *

# Create your views here.
def store(request):
     products = Product.objects.all()
     context = {'products':products}
     return render(request, 'store/store.html', context)



def cart(request):
     if request.user.is_authenticated:
          customer = request.user.customer
          cart, created = Cart.objects.get_or_create(customer=customer, complete=False) #fetch or create a cart
          items = cart.orderproduct_set.all() # objects of OrderProduct class
     else:
          items = []
          cart={"cart_total_items_quantity":0, "cart_total_amount":0}

     context = {'items':items, 'cart':cart}
     return render(request, 'store/cart.html', context)



def checkout(request):
     if request.user.is_authenticated:
          customer = request.user.customer
          cart, created = Cart.objects.get_or_create(customer=customer, complete=False) #fetch or create a cart
          items = cart.orderproduct_set.all() # objects of OrderProduct class
     else:
          items = []
          cart={"cart_total_items_quantity":0, "cart_total":0}

     context = {'items':items, 'cart':cart}
     return render(request, 'store/checkout.html', context)



def updateItem(request):
     return JsonResponse('Item was added', safe=False)