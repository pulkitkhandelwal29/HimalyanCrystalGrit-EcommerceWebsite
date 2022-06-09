from django.shortcuts import render,redirect,get_object_or_404
from store.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request,product_id):
    product = Product.objects.get(id=product_id) #get the product
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request)) # get the cart using cart_id present in session
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
        cart_id = _cart_id(request)
        )

    cart.save()

    try:
        cart_item = CartItem.objects.get(product = product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
        product = product,
        quantity = 1,
        cart = cart,
        )
        cart_item.save()
    return redirect('cart')


def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product, id = product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


def remove_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product = product, cart = cart)
    cart_item.delete()
    return redirect('cart')



def cart(request, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart)
        for cart_item in cart_items:
            quantity += cart_item.quantity

    except ObjectDoesNotExist:
        pass

    context = {
    'quantity' : quantity,
    'cart_items' : cart_items,
    }
    return render(request, 'store/cart.html',context)
