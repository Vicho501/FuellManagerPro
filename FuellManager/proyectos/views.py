from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import RegistroProduccion, Produto
from .forms import RegistroProduccionFrom

# Create your views here.

#decimos que nesesita registrarse con el @login_required
@login_required
#registramos el producto
def registrar_produccion(request):
    if request.method=='POST':
        from =RegistroProduccionFrom(request.POST)
        if from.is_valid():
            registro=from.save(commit=False)
            registro.operador=request.User
            registro.save()
        
    else:
        from=RegistroProduccionFrom()
    return render(request, 'registro/registrar_produccion.html',{'from':from})

