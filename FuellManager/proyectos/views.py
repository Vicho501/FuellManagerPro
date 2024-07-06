from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import RegistroProduccion, Produto
from .forms import RegistroProduccionForm

# Create your views here.
def home(request):
    title = "Inicio"

    data = {
        "title" : title
    }

    return render(request, 'home.html',data)

#decimos que nesesita registrarse con el @login_required
@login_required
#registramos el producto
def registrar_produccion(request):
    if request.method=='POST':
        form = RegistroProduccionFrom(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.operador=request.User
            registro.save()
        
    else:
        form = RegistroProduccionForm()
    
    return render(request, 'registro/registrar_produccion.html',{'form':form})

