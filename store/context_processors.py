from .cart import Cart
from .models import Customer


def cart(request):
    return {"cart": Cart(request)}

def wishlist(request):
    if request.user.is_authenticated:
        customer = Customer.objects.get(user=request.user)
        return {"wishlist": len(customer.wishlist)}
    return {"wishlist": 0}
