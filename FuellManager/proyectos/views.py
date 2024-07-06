from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import RegistroProduccion, Producto
from .forms import RegistroProduccionForm, EditarProduccionForm

# Create your views here.
def home(request):
    title = "Inicio"

    data = {
        "title" : title
    }

    return render(request, 'home.html',data)

#decimos que nesesita registrarse con el @login_required

#registramos el producto
def registrar_produccion(request):
    if request.method == 'POST':
        form = RegistroProduccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_registros_produccion')
    else:
        form = RegistroProduccionForm()

    return render(request, 'registrar_produccion.html', {'form': form})


def editar_produccion(request, name):
    product = get_object_or_404(RegistroProduccion, name=name)
    
    if request.method == 'POST':
        form = EditarProduccionForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirigir a la lista de proyectos u otra página después de guardar
    else:
        form = EditarProduccionForm(instance=product)
    
    return render(request, 'editar_produccion.html', {'form': form})