from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Perro  # Cambiado de Producto a Perro
from .forms import PerroForm  # Cambiado de ProductoForm a PerroForm

def index(request):
    return render(request, 'app_perros/index.html', { # Posiblemente quieras cambiar la ruta del template
        'perros': Perro.objects.all() # Cambiado de 'productos' a 'perros'
    })

def view_perro(request, id):
    perro = get_object_or_404(Perro, pk=id) # Cambiado de Producto a Perro
    return redirect('index') # Esto redireccionará a la lista principal después de "ver" (aunque el 'view' original también solo redireccionaba)

def add(request):
    success = False
    if request.method == 'POST':
        form = PerroForm(request.POST) # Cambiado de ProductoForm a PerroForm
        if form.is_valid():
            form.save()
            success = True
            form = PerroForm() # Resetear el formulario después de guardar
    else:
        form = PerroForm() # Cambiado de ProductoForm a PerroForm
    return render(request, 'app_perros/add.html', { # Posiblemente quieras cambiar la ruta del template
        'form': form,
        'success': success
    })

def edit(request, id):
    perro = get_object_or_404(Perro, pk=id) # Cambiado de Producto a Perro
    success = False
    if request.method == 'POST':
        form = PerroForm(request.POST, instance=perro) # Cambiado de ProductoForm a PerroForm
        if form.is_valid():
            form.save()
            success = True
    else:
        form = PerroForm(instance=perro) # Cambiado de ProductoForm a PerroForm
    return render(request, 'app_perros/edit.html', { # Posiblemente quieras cambiar la ruta del template
        'form': form,
        'success': success
    })

def borrar(request, id):
    perro = get_object_or_404(Perro, pk=id) # Cambiado de Producto a Perro
    perro.delete()
    return HttpResponseRedirect(reverse('index'))