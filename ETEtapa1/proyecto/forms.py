from django import forms
from .models import Proveedores
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from django.forms import ModelForm

class ProveedoresForm(forms.ModelForm):

    class Meta:
        model = Proveedores
        fields = [
        'NumeroIdentificacion',
        'NombreProveedor',
        'TelefonoProveedor',
        'DireccionProveedor',
        'EmailProveedor',
        'PaisProveedor',
        'ContraseñaProveedor']
        labels = {
        'NumeroIdentificacion': 'Numero de Identificacion',
        'NombreProveedor': 'Nombre del proveedor',
        'TelefonoProveedor': 'Telefono del Proveedor',
        'DireccionProveedor': 'Direccion del Proveedor',
        'EmailProveedor': 'Email del Proveedor',
        'PaisProveedor': 'Pais del Proveedor',
        'ContraseñaProveedor': 'Contraseña del Proveedor'}
        widgets={
        'NumeroIdentificacion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Numero de Identificacion',
                    'id': 'NumeroId'}
        ),
        'NombreProveedor': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Nombre',
                    'id': 'Nombre'}
        ),
        'TelefonoProveedor': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Telefono',
                    'id': 'Telefono'}
        ),
        'DireccionProveedor': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Direccion',
                    'id': 'Direccion'}
        ),
        'EmailProveedor': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Email',
                    'id': 'Email'}
        ),
        'PaisProveedor': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Pais',
                    'id': 'Pais'}
        ),
        'ContraseñaProveedor': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Contraseña',
                    'id': 'Contraseña'}
        )
        }
