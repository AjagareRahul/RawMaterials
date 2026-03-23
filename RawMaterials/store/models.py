from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    bulk_price = models.DecimalField(max_digits=10, decimal_places=2)

    stock = models.PositiveIntegerField()
    unit = models.CharField(max_length=50)

    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField('CartItem', blank=True)

class CartItem(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    total_price=models.DecimalField(max_digits=10, decimal_places=2)
    status=models.CharField(max_length=20, default='pending')
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"