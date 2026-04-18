from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Cart,CartItem
from materials.models import Material


@login_required
def cart_view(request):
    user=request.user
    
    try:
        cart=Cart.objects.get(user=user)
        cart_items=cart.cartitem_set.all()
    except Cart.DoesNotExist:
        cart_items=[]
        cart=None
    
    total=0
    for item in cart_items:
        total +=item.total_price()
        
    return render(request,'account/cart.html',{'cart_items':cart_items,'total':total})

@login_required
def add_to_cart(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    user = request.user
    
    cart, _ = Cart.objects.get_or_create(user=user)
    
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        material=material,
        defaults={'quantity': 1}
    )
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart_view')

@login_required
def remove_from_cart(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    user = request.user
    
    try:
        cart = Cart.objects.get(user=user)
        cart_item = CartItem.objects.get(cart=cart, material=material)
        cart_item.delete()
    except (Cart.DoesNotExist, CartItem.DoesNotExist):
        pass
    
    return redirect('home_materials')

@login_required
def update_cart(request,item_id,action):
    cart_item=get_object_or_404(CartItem, id=item_id)
    
    if action == 'increase':
        cart_item.quantity +=1
    elif action == 'decrease':
        cart_item.quantity -=1
        
        if cart_item.quantity <=0:
            cart_item.delete()
            return redirect('cart_view')
    cart_item.save()
    return redirect('cart_view')

@login_required
def remove_item(request,item_id):
    cart_item=get_object_or_404(CartItem,id=item_id)
    cart_item.delete()
    
    return redirect('cart_view')

        
    