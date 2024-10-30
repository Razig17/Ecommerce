from django.shortcuts import render, redirect
from .models import Product, Customer
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegisterForm, CustomerForm
from .cart import Cart
from django.http import JsonResponse

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



def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in")
            return redirect("store")
        else:
            messages.success(request, "Invalid credentials")
            return redirect("store")
    format = RegisterForm()
    return render(request, "login.html" , {"form": format})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("store")


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "You’ve successfully registered! Please complete your profile")
            return redirect("my_account")
        else:
            messages.error(request, "Please correct the error .")
    else:
        form = RegisterForm()
    return render(request, "login.html" , {"form": form})


def my_account(request):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in")
        return redirect("login")
    
    elif request.method == 'POST':
        user = Customer.objects.get(user__id=request.user.id)   
        form = CustomerForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Account updated")
        else:
            for msg in form.errors:
                messages.error(request, msg)
                messages.error(request, form.errors[msg])
            render(request, "my_account.html" , {"form": form})

    user = Customer.objects.get(user__id=request.user.id)        
    form = CustomerForm(instance=user)
    return render(request, "my_account.html" , {"form": form})


def cart(request):
    return render(request, "cart.html" , {})


def add_to_cart(request, id):
    if request.method == "POST":    
        qty = request.POST.get('qty', 1)
        cart = Cart(request)
        product = Product.objects.get(id=id)
        cart.add_item(product, (qty))
        msg = 'Product added to cart'
        if int(qty) > 1:
            msg = 'Products added to cart'
        return JsonResponse({"qty": cart.__len__(), "total_price": cart.get_total_price(), "msg": msg})
    
def remove_from_cart(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove_item(product)
    messages.success(request, "Product removed from cart")
    return redirect("cart")

def update_cart(request, id):
    if request.method == "POST":
        qty = request.POST.get('qty', 1)
        cart = Cart(request)
        product = Product.objects.get(id=id)
        cart.update_quantity(product, int(qty))
        msg = 'Product quantity updated'
        return JsonResponse({"total_price": cart.get_total_price(), "msg": msg, "qty": cart.__len__()})

def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    messages.success(request, "Cart cleared")
    return redirect("cart")

