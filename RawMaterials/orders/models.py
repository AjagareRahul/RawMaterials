from django.db import models
from django.conf import settings
# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Cart -{self.user.username}"

class CartItem(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    material=models.ForeignKey('materials.Material', on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    
    
    def __str__(self):
        return f"{self.material} ({self.quantity})"

    def total_price(self):
        user = self.cart.user

        if user.role == 'contractor':
            return self.quantity * self.material.bulk_price
        else:
            return self.quantity * self.material.price
