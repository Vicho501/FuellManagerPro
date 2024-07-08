import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import RegistroProduccion, Producto
from .forms import RegistroProduccionForm, EditarProduccionForm
from django.db.models import Sum

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
            registro = form.save(commit=False)  # Define `registro` correctamente aquí
            registro.operador = request.user
            form.save()
            registro.save()
            total_stored = calcular_total_stored()  # Calcula el total almacenado
            send_slack_notification(registro, total_stored)
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

def send_slack_notification(registro, total_stored):
    webhook_url = 'https://hooks.slack.com/services/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'  #Agregamos la URL de webhook de Slack
    message = (
        f"Fecha hora: {registro.hora_registro.strftime('%Y-%m-%d %H:%M:%S')} "
        f"CÓDIGO PLANTA: {registro.codigo_combustible.planta.codigo} – "
        f"Nuevo Registro de Producción – "
        f"CÓDIGO COMBUSTIBLE: {registro.codigo_combustible.codigo} "
        f"{registro.litros_producidos} litros registrados | "
        f"Total Almacenado: {total_stored} litros"
    )
    payload = {
        "text": message
    }
    #PARA QUE FUNCIONE EL REQUEST HAY QUE HACER pip install requests, ademas de inportar la biblioteca (ya lo hice)
    response = requests.post(webhook_url, json=payload)
    
    if response.status_code != 200:
        raise ValueError(
            f'Request to Slack returned an error {response.status_code}, the response is:\n{response.text}'
        )


def calcular_total_stored():    
    total_stored = RegistroProduccion.objects.aggregate(Sum('litros_producidos'))['litros_producidos__sum']
    
    return total_stored