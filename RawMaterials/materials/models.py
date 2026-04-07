from django.db import models

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