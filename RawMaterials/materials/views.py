from django.shortcuts import render, redirect, get_object_or_404
from .models import Material
from .forms import MaterialForm

def home_materials(request):
    materials = Material.objects.select_related('category').all()
    categories = {}
    for material in materials:
        cat_name = material.category.name if material.category else 'Uncategorized'
        if cat_name not in categories:
            categories[cat_name] = []
        categories[cat_name].append(material)
    return render(request, 'account/home.html', {'categories': categories})

def add_materials(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home_materials')
    else:
        form = MaterialForm()
    
    return render(request, 'account/add_materials.html', {'form': form})

def update_materials(request, pk):
    material = get_object_or_404(Material, pk=pk)
    
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES, instance=material)
        if form.is_valid():
            form.save()
            return redirect('home_materials')
    else:
        form = MaterialForm(instance=material)
    
    return render(request, 'account/add_materials.html', {'form': form})

def delete_material(request,id):
    material=get_object_or_404(Material,id=id)
    material.delete()
    return redirect('home_materials')