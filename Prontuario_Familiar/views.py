from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect

from Home.urls import home
from .models import Responsavel, Prontuario, GrupoFamiliar
from .forms import ProntuarioForm, ResponsavelForm, GrupoFamiliarForm

# Create your views here.
@login_required
def RegistrarResponsavel(request):
    formResponsavel = ResponsavelForm(request.POST or None)
    
    if(formResponsavel.is_valid()):
        form.save()
        messages.success(request, 'Responsável Registrado com Sucesso!')
        return redirect('../RegistrarProntuario')
    return render(request, 'RegistroResponsavel')

def AtualizarRegistro(request, id):
    

@login_required
def DeletarProntuario(request, id):
    prontuario = get_object_or_404(Prontuario, pk=id)
    prontuario.delete()
    return redirect('../../ListarProntuarios')
