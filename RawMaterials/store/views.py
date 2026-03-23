from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, Cart, CartItem


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_details.html', {'product': product})

def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        return HttpResponse("Please login first")
        
    user=request.user
    
    product=get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    if quantity > product.stock:
        return HttpResponse("Not enough stock available")
    
   cart,created=Cart.objects.get_or_create(user=user)
   