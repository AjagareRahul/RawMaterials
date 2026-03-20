from store.views import *
from django.urls import path
urlpatterns = [
    path('', home, name='home'),
    path('products/<int:product_id>/', product_details, name='product_details'),
]