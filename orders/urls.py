from django.urls import path

from .views import cart_view, update_cart, remove_item, add_to_cart, remove_from_cart

urlpatterns=[
    path('cart/',cart_view,name='cart_view'),
    path('update_cart/<int:item_id>/<str:action>/',update_cart,name='update_cart'),
    path('remove_item/<int:item_id>/',remove_item,name='remove_item'),
    path('add_to_cart/<int:material_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:material_id>/', remove_from_cart, name='remove_from_cart'),
]