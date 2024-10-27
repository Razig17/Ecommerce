from django.shortcuts import render
from .models import Product


def index(request):
    return render(request, "index.html" , {})


def store(request):
    query = request.GET.get('query', (""))
    category = request.GET.get('category', 0)
    if category == "0":
        products = Product.objects.filter(name__contains=query)
    elif category != 0:
        products = Product.objects.filter(category__name=category, name__contains=query)
    else:
        products = Product.objects.all()
    return render(request, "store.html" , {"products": products})


def smartphones(request):
    products = Product.objects.filter(category__name="smartphones")
    return render(request, "smartphones.html" , {"products": products})


def laptops(request):
    products = Product.objects.filter(category__name="laptops")
    return render(request, "laptops.html" , {"products": products})


def product(request, id):
    product = Product.objects.get(id=id)
    return render(request, "product.html" , {"product": product})
