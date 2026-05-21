from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Material(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='materials', null=True, blank=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bulk_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=20)
    image = models.ImageField(upload_to='materials/', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name
