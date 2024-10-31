from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save


# Category model
class Category(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
	    verbose_name_plural = 'categories'

# Product model
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='product/images/', default='images/default.jpg')

    def __str__(self):
        return self.name
    
    def is_available(self):
        return self.stock > 0
    
# Customer model
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username
    

# Order model
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)   
    created_at = models.DateTimeField(default=timezone.now)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    completed = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    city = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=10 ,blank=True, null=True)
    is_shipped = models.BooleanField(default=False)
    shipped_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return str(self.id)

#Order item model
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return f"Order item {self.product.name} for order {self.order.id}"
    

# Create a signal to create a customer when a user is created
def create_customer(sender, instance, created, **kwargs):
    if created:
        customer = Customer(user=instance)
        customer.save()

post_save.connect(create_customer, sender=User)
