from django.shortcuts import render
from store.models import Product
from banner.models import Banner

def home(request):
    products = Product.objects.all().filter(is_available=True)
    banners = Banner.objects.all()

    context = {
    'products' : products,
    'banners' : banners,
    }

    return render(request, 'home.html',context)
