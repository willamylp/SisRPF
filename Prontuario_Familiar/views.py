from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect

from Home.urls import home
from .models import Responsavel, Prontuario, GrupoFamiliar
from .forms import ProntuarioForm, ResponsavelForm, GrupoFamiliarForm

# Create your views here.
@login_required
def RegistrarProntuario(request):
    formProntuario = ResponsavelForm(request.POST or None)
    
    if(formProntuario.is_valid()):
        formProntuario.save()
        messages.success(request, 'Prontuário Registrado com Sucesso!')
        return redirect('../RegistroResponsavel')
    return render(request, 'registros/form_prontuario.html', {'formProntuario': formProntuario})


@login_required
def RegistrarResponsavel(request):
    formResponsavel = ResponsavelForm(request.POST or None)
    
    if(formResponsavel.is_valid()):
        formResponsavel.save()
        messages.success(request, 'Responsável Registrado com Sucesso!')
        return redirect('../RegistroGrupoFamiliar')
    return render(request, 'registros/form_responsavel.html', {'formResponsavel': formResponsavel})

@login_required
def RegistrarGrupoFamiliar(request):
    formGrupoFamiliar = GrupoFamiliarForm(request.POST or None)

    if(formGrupoFamiliar.is_valid()):
        formGrupoFamiliar.save()
        messages.success(request, 'Membro do Grupo Familiar Registrado com Sucesso!')
        return redirect('RegistroGrupoFamiliar')
    return render(request, 'registros/form_integrantes.html', {'formGrupoFamiliar': formGrupoFamiliar})

@login_required
def AtualizarProntuario(request, id):
    prontuario = get_object_or_404(Prontuario, pk=id)
    form = ProntuarioForm(request.POST or None, instance=prontuario)
    if(form.is_valid()):
        form.save()
        return redirect('../../ListarProntuarios')

@login_required
def AtualizarResponsavel(request, id):
    responsavel = get_object_or_404(Responsavel, pk=id)
    form = ProntuarioForm(request.POST or None, instance=responsavel)
    if(form.is_valid()):
        form.save()
        return redirect('../../ListarProntuarios')

@login_required
def AtualizarGrupoFamiliar(request, id):
    integrante = get_object_or_404(Responsavel, pk=id)
    form = ProntuarioForm(request.POST or None, instance=integrante)
    if(form.is_valid()):
        form.save()
        return redirect('../../ListarProntuarios')

@login_required
def BuscarProntuario(request):
    pass

@login_required
def DeletarProntuario(request, id):
    prontuario = get_object_or_404(Prontuario, pk=id)
    prontuario.delete()
    return redirect('../../ListarProntuarios')
