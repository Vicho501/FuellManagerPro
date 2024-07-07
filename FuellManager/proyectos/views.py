from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import RegistroProduccion, Producto
from .forms import RegistroProduccionForm, EditarProduccionForm

# Create your views here.
def home(request):
    title = "Inicio"

    data = {
        "title" : title
    }

    return render(request, 'home.html',data)

def exit(request):
    logout(request)
    return redirect('home')

@login_required
def producciones(request):
    titulo = "Lista de Producciones"

    producciones = RegistroProduccion.objects.all()

    return render(request, 'producciones.html', {
        'producciones': producciones,
        'titulo': titulo,
        })

#decimos que nesesita registrarse con el @login_required
@login_required
#registramos el producto
def registrar_produccion(request):
    if request.method == 'POST':
        form = RegistroProduccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producciones')
    else:
        form = RegistroProduccionForm()

    return render(request, 'registrar_produccion.html', {'form': form})

@login_required
def editar_produccion(request, id):
    product = get_object_or_404(RegistroProduccion, id=id)
    
    if request.method == 'POST':
        form = EditarProduccionForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('producciones')  # Redirigir a la lista de proyectos u otra página después de guardar
    else:
        form = EditarProduccionForm(instance=product)
    
    return render(request, 'editar_produccion.html', {'form': form})

def eliminar(request, id):
    product = get_object_or_404(RegistroProduccion, id=id)
    product.delete()
    return redirect('producciones') 
