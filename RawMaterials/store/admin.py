from django.contrib import admin
from .models import Product, Category, Cart, CartItem

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'bulk_price', 'stock', 'unit')
    search_fields = ('name', 'description')
    list_filter = ('category',)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartItem)