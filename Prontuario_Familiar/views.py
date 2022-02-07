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
    formP = ProntuarioForm(request.POST or None)
    formR = ResponsavelForm(request.POST or None)

    if(formP.is_valid()):
        formP.save()
        if(request.POST['nome'] != ''):
            Responsavel.objects.create(
                prontuario = Prontuario.objects.get(
                    pk=Prontuario.objects.filter(numero=request.POST['numero'])[:1]
                ),
                nome = request.POST['nome'],
                dt_nascimento = request.POST['dt_nascimento'],
                cpf = request.POST['cpf'],
                logradouro = request.POST['logradouro'],
                num_endereco = request.POST['num_endereco'],
                complemento = request.POST['complemento'],
                bairro = request.POST['bairro'],
                ponto_referencia = request.POST['ponto_referencia'],
            ).save()
            
        elif(request.POST['nome'] == ''):
            return render(
                request, 
                'registros/form_prontuario.html', 
                {'formP': formP, 'formR': formR}
            )
        return redirect('../RegistroGrupoFamiliar')
    return render(
        request,
        'registros/form_prontuario.html',
        {'formP': formP, 'formR': formR}
    )
        

    
# @login_required
# def RegistrarProntuario(request):
#     formP = ProntuarioForm(request.POST or None)
#     formR = ResponsavelForm(request.POST or None)

#     if((formP.is_valid()) and (formR.is_valid())):
#         formP.save()
#         formR.save()
#         return redirect('../RegistroGrupoFamiliar')
#     return render(request, 'registros/form_prontuario.html', {'formP': formP, 'formR': formR})

@login_required
def RegistrarResponsavel(request):
    formResponsavel = ResponsavelForm(request.POST or None)
    
    if(formResponsavel.is_valid()):
        formResponsavel.save()
        return redirect('../RegistroGrupoFamiliar')
    return render(request, 'registros/form_responsavel.html', {'formResponsavel': formResponsavel})

@login_required
def RegistrarGrupoFamiliar(request):
    formGrupoFamiliar = GrupoFamiliarForm(request.POST or None)

    if(formGrupoFamiliar.is_valid()):
        formGrupoFamiliar.save()
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
    return redirect('../ListarProntuarios')
