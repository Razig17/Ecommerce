from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("store/", views.store, name="store"),
    path("store/smartphones", views.smartphones, name="smartphones"),
    path("store/laptops", views.laptops, name="laptops"),
    path("store/<int:id>", views.product, name="product"),
]
