from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.shortcuts import render
from .models import Product, Payment
from cart.cart import Cart
import time
import datetime
# Create your views here.
def func1(request):
  items = Product.objects.filter().order_by('name')
  cart = Cart(request)
  return render(request, 'blog/index.html', {'items': items, 'total_price' : cart.summary()})
    
def func2(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart = Cart(request)
    return render(request, 'blog/index1.html', {'product': product, 'total_price' : cart.summary()})
def func3(request):
    cart = Cart(request)
    return render(request, 'blog/index2.html', {'total_price' : cart.summary()})

def func4(request):
    cart = Cart(request)
    return render(request, 'blog/index4.html', {'cart' : cart, 'total_price' : cart.summary()})


def account_logout(request):
      """
      Logout and redirect to the main page.
      """
      logout(request)
      return redirect('/shop1')

def add_to_cart(request):
    product_id = request.POST.get('product_id')[0]   
    product = Product.objects.get(pk=product_id)
    cart = Cart(request)
    quantity = 1
    cart.add(product, product.price, quantity)
    return HttpResponse(cart.summary())

def remove_from_cart(request):
    product_id = request.POST.get('product_id')[0]
    print(product_id)
    product = Product.objects.get(pk=product_id)
    cart = Cart(request)
    cart.remove(product)
    return HttpResponse(cart.summary())

@csrf_exempt
def paypal_success(request):
    cart = Cart(request)
    payment = Payment(payment_type=1, date=datetime.date.today(), cost=cart.summary(), user=request.user)
    payment.save()
    cart.clear()
    return HttpResponse("Money is mine. Thanks.")
  
  
@login_required
def paypal_pay(request):
      """
      Page where we ask user to pay with paypal.
      """
      cart = Cart(request)
      products = list()
      for elem in cart:
        products.append(elem.product.name)
      paypal_dict = {
          "business": "ruslan_cimbalyuk-facilitator@mail.ru",
          "amount": 1,
          "currency_code": "RUB",
          "item_name": products,
          "invoice": "INV-" + str(int(time.time())),
          "notify_url": reverse('paypal-ipn'),
          "return_url": "http://localhost:8000/payment/success/",
          "cancel_return": "http://localhost:8000/payment/cart/",
          "custom": str(request.user.id)
      }
  
      # Create the instance.
      form = PayPalPaymentsForm(initial=paypal_dict)
      context = {"form": form, "paypal_dict": paypal_dict}
      return render(request, "blog/payment.html", context) 
