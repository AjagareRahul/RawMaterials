"""
URL configuration for RawMaterials project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('', include('materials.urls')),
    path('', include('orders.urls')),
]
