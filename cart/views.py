from http.client import responses

from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .cart import Cart
from shop.models import Product
from django.http import JsonResponse


def cart_summary(request):
    cart=Cart(request)
    cart_products=cart.get_products()
    quantities=cart.get_quantities
    totals=cart.cart_total()
    return render(request, 'cart/cart_summary.html',
                  {'cart_products':cart_products, 'quantities':quantities, 'totals':totals})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id= int(request.POST.get('product_id'))
        product_qty=int(request.POST.get('product_qty'))
        product= get_object_or_404(Product, id=product_id)

        cart.add(product=product, quantity=product_qty)

        cart_quantity=cart.__len__()

        # response= JsonResponse({'Product Name':product.name})
        response=JsonResponse({'qty':cart_quantity})
        messages.success(request, f'Item {product.name} has been added to cart')
        return response

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)

        response = JsonResponse({'product': product_id})
        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id= int(request.POST.get('product_id'))
        product_qty=int(request.POST.get('product_qty'))


        cart.update(product=product_id, quantity=product_qty)

        response= JsonResponse({'qty':product_qty})
        return response


def checkout(request):
    # Get the cart
    cart = Cart(request)
    cart_products = cart.get_products()
    quantities = cart.get_quantities()
    totals = cart.cart_total()
    return render(request, "cart/checkout.html",
                  {"cart_products": cart_products, "quantities": quantities, "totals": totals})



