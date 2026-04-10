from django.shortcuts import render, redirect, get_object_or_404
from .models import Material
from .forms import MaterialForm

def home_materials(request):
    material = Material.objects.all()
    return render(request, 'account/home.html', {'material': material})

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
    return redirect('add_materials')