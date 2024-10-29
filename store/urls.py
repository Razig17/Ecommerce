from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("store/", views.store, name="store"),
    path("store/smartphones", views.smartphones, name="smartphones"),
    path("store/laptops", views.laptops, name="laptops"),
    path("store/<int:id>", views.product, name="product"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("my_account/", views.my_account, name="my_account"),
]
