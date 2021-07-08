from django.shortcuts import render, redirect
from .models import Proveedores
from .forms import ProveedoresForm
# Create your views here.
def hub(request):
    Proveedor = Proveedores.objects.all()
    return render(request, 'proyecto/hub.html')

def index(request):
    Proveedor = Proveedores.objects.all()
    context = {'Proveedor': Proveedor}
    return render(request, 'proyecto/index.html', context)

def subir(request):
    if request.method == "POST":
        form = ProveedoresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProveedoresForm()
    context = {'form' : form}
    return render(request, 'proyecto/subir.html', context)

def editar(request, proveedores_id):
    proveedores = Proveedores.objects.get(id=proveedores_id)
    if request.method == "POST":
        form = ProveedoresForm(request.POST, instance=proveedores)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ProveedoresForm(instance=proveedores)

    context = {"form" : form}
    return render(request, "proyecto/editar.html", context)

def eliminar(request, proveedores_id):
    proveedores = Proveedores.objects.get(id=proveedores_id)
    proveedores.delete()
    return redirect("index")
