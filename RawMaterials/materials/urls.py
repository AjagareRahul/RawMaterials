from django.urls import path
from materials.views import home_materials, add_materials, update_materials,delete_material

urlpatterns = [
    path('', home_materials, name='home_materials'),
    path('add_materials/', add_materials, name='add_materials'),
    path('update_materials/<int:pk>/', update_materials, name='update_materials'),
    path('delete/<int:id>/',delete_material,name='delete_material'),
]