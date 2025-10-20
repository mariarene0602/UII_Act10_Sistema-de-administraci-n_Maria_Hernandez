# app_perros/forms.py

from django import forms
from .models import Perro 

class PerroForm(forms.ModelForm):
    """
    Formulario basado en el modelo Perro, adaptado a tu negocio.
    Sin los campos 'color' y 'edad'.
    """
    class Meta:
        model = Perro
        fields = [
            'nombre',
            'raza',
            'fecha_nacimiento',
            'descripcion',
        ]
        labels = {
            'nombre': 'Nombre del Perro',
            'raza': 'Raza del Perro',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'descripcion': 'Notas Adicionales',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'raza': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), 
        }