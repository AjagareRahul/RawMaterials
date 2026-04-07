from django.urls import path
from materials.views import home_materials, add_materials, update_materials

urlpatterns = [
    path('home_materials/', home_materials, name='home_materials'),
    path('add_materials/', add_materials, name='add_materials'),
    path('update_materials/<int:pk>/', update_materials, name='update_materials'),
]