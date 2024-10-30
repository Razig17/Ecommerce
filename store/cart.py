from decimal import Decimal

class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("cart")
        if "cart" not in request.session:
            cart = self.session["cart"] = {}
        self.cart = cart

    def add_item(self, item, quantity):
        item_id = str(item.id)

        if item_id not in self.cart:
            self.cart[item_id] = {"id": item.id, "quantity": int(quantity), "price": float(item.price), "name": item.name, "image": item.image.url}
        else:
            
            self.cart[item_id]["quantity"] += int(quantity)
        self.save()

    def remove_item(self, item):
        item_id = str(item.id)
        if item_id in self.cart:
            del self.cart[item_id]
            self.save()

    def get_total_price(self):
        return sum(item["price"] * item["quantity"] for item in self.cart.values())
    
    def update_quantity(self, item, quantity):
        item_id = str(item.id)
        if item_id in self.cart:
            self.cart[item_id]["quantity"] = quantity
            self.save()
    
    def clear(self):
        self.session["cart"] = {}
        self.save()

    def save(self):
        self.session.modified = True
    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())
    def get_total_items(self):
        return sum(item["quantity"] for item in self.cart.values())
    