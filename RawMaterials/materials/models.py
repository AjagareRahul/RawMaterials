from django.db import models
from django.conf import settings

class Material(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bulk_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=20)
    image = models.ImageField(upload_to='materials/', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    
from django.conf import settings

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    material=models.ForeignKey('materials.Material', on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    
    