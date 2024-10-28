from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegisterForm

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


# def register_user(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         email = request.POST["email"]
#         password = request.POST["password"]
#         if User.objects.filter(username=username).exists():
#             messages.success(request, "That username is taken")
#             return redirect("register")
#         else:
#             if User.objects.filter(email=email).exists():
#                 messages.success(request, "That email is being used")
#                 return redirect("register")
#             else:
#                 user = User.objects.create_user(username=username, email=email, password=password)
#                 user.save()
#                 login(request, user)
#                 messages.success(request, "You are now logged in")
#                 return redirect("store")
#     return render(request, "login.html" , {})

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "You are now logged in")
            return redirect("store")
        else:
            messages.error(request, "Please correct the error .")
    else:
        form = RegisterForm()
    return render(request, "login.html" , {"form": form})
