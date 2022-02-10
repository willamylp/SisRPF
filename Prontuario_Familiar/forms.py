from tkinter import Widget
from .models import Responsavel, Prontuario, GrupoFamiliar
from django import forms
from django.forms import ModelForm

class DateInput(forms.DateInput):
    input_type = 'date'


class ResponsavelForm(ModelForm, forms.Form):
    class Meta:
        model = Responsavel
        fields = '__all__'
        widgets = {}


class ProntuarioForm(ModelForm, forms.Form):
    class Meta:
        model = Prontuario
        fields = '__all__'
        widgets = {}

class GrupoFamiliarForm(ModelForm, forms.Form):
    class Meta:
        model = GrupoFamiliar
        fields = '__all__'
        widgets = {}
