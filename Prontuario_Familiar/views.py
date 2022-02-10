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
        if('nome' in request.POST):
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
            
        #elif(request.POST['nome'] == ''):
        else:
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

@login_required
def RegistrarResponsavel(request):
    formResponsavel = ResponsavelForm(request.POST or None)
    
    if(formResponsavel.is_valid()):
        formResponsavel.save()
        return redirect('../RegistroGrupoFamiliar')
    return render(request, 'registros/form_responsavel.html', {'formResponsavel': formResponsavel})

@login_required
def RegistrarGrupoFamiliar(request):
    formGF = GrupoFamiliarForm(request.POST or None)
    resp = Responsavel.objects.all().last()
    #print('\n >>> {} '.format(request.POST['responsavel']))
    if('nome_integrante' in request.POST):
        GrupoFamiliar.objects.create(
            responsavel = Responsavel.objects.all().last(),
            nome_integrante = request.POST['nome_integrante'],
            parentesco = request.POST['parentesco'],
            dt_nascimento = request.POST['dt_nascimento'],
            sexo = request.POST['sexo'],
            estado_civil = request.POST['estado_civil'],
            naturalidade = request.POST['naturalidade'],
            escolaridade = request.POST['escolaridade'],
            ativ_economica = request.POST['ativ_economica'],
            renda = request.POST['renda'],
        ).save()
    else:
        return render(
            request, 
            'registros/form_integrantes.html', 
            {'formGF': formGF, 'responsavel': resp}
        )
    return redirect('RegistroGrupoFamiliar')


    # if(formGF.is_valid()):
    #     formGF.save()
    #     return redirect('RegistroGrupoFamiliar')
    # return render(request, 'registros/form_integrantes.html', {'formGF': formGF, 'responsavel': resp})

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
