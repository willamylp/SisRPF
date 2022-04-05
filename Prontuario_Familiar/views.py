from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect

from Home.urls import home
from .models import Responsavel, Prontuario, GrupoFamiliar
from .forms import ProntuarioForm, ResponsavelForm, GrupoFamiliarForm


@login_required
def RegistrarProntuario(request):
    formP = ProntuarioForm(request.POST or None)
    formR = ResponsavelForm(request.POST or None)
    ultimoReg = Prontuario.objects.all().last()

    if(formP.is_valid()):
        formP.save()
        if('nome' in request.POST):
            Responsavel.objects.create(
                prontuario = Prontuario.objects.get(
                    pk=Prontuario.objects.filter(
                        numero=request.POST['numero'])[:1]
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
        else:
            return render(
                request, 
                'registros/form_prontuario.html', 
                {'formP': formP, 'formR': formR, 'ultimoRegistro': ultimoReg}
            )
        id_resp = Responsavel.objects.latest('pk').pk
        return redirect(f'../RegistroGrupoFamiliar/{id_resp}')
    return render(
        request,
        'registros/form_prontuario.html',
        {'formP': formP, 'formR': formR, 'ultimoRegistro': ultimoReg}
    )

@login_required
def RegistrarGrupoFamiliar(request, id):
    formGF = GrupoFamiliarForm(request.POST or None)
    nome_resp = Responsavel.objects.filter(id=id)[0]
    integrantes = GrupoFamiliar.objects.filter(responsavel_id=id)

    if('nome_integrante' in request.POST):
        GrupoFamiliar.objects.create(
            responsavel_id = id,
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
            'registros/form_integrantes.html', {
                'formGF': formGF,
                'responsavel': nome_resp,
                'grupoF': integrantes
            }
        )
    return redirect(f'../RegistroGrupoFamiliar/{id}')

@login_required
def AtualizarProntuario(request, id_p, id_r):
    pront = get_object_or_404(Prontuario, pk=id_p)
    resp = get_object_or_404(Responsavel, pk=id_r)

    formP = ProntuarioForm(request.POST or None, instance=pront)
    formR = ResponsavelForm(request.POST or None, instance=resp)

    if(formP.is_valid()):
        formP.save()
        if('nome' in request.POST):
            Responsavel.objects.create(
                prontuario=Prontuario.objects.get(
                    pk=Prontuario.objects.filter(
                        numero=request.POST['numero'])[:1]
                ),
                nome=request.POST['nome'],
                dt_nascimento=request.POST['dt_nascimento'],
                cpf=request.POST['cpf'],
                logradouro=request.POST['logradouro'],
                num_endereco=request.POST['num_endereco'],
                complemento=request.POST['complemento'],
                bairro=request.POST['bairro'],
                ponto_referencia=request.POST['ponto_referencia'],
            ).save()
        else:
            return render(
                request,
                'registros/form_prontuario.html',
                {'formP': formP, 'formR': formR}
            )
        return redirect(f'../../RegistroGrupoFamiliar/{id_r}')
    return render(
        request,
        'registros/form_prontuario.html',
        {'formP': formP, 'formR': formR}
    )

@login_required
def AtualizarGrupoFamiliar(request, id):
    integrante = get_object_or_404(Responsavel, pk=id)
    form = ProntuarioForm(request.POST or None, instance=integrante)
    if(form.is_valid()):
        form.save()
        return redirect('../../ListarProntuarios')

@login_required
def ListarProntuarios(request):
    pront = Prontuario.objects.all().values()
    resp = Responsavel.objects.all().values()
    grupoF = GrupoFamiliar.objects.all().values()

    return render(
        request,
        'listagem/list_prontuarios.html', {
            'prontuarios': pront,
            'responsaveis': resp,
            'grupoF': grupoF
        }
    )

@login_required
def BuscarProntuario(request):
    pass

@login_required
def DeletarIntegrante(request, id_resp, id):
    integrante = get_object_or_404(GrupoFamiliar, pk=id)
    integrante.delete()
    
    GrupoFamiliar.objects.filter(responsavel_id=id)

    return redirect(f'../../RegistroGrupoFamiliar/{id_resp}')

@login_required
def DeletarProntuario(request, id):
    prontuario = get_object_or_404(Prontuario, pk=id)
    prontuario.delete()
    return redirect('../ListarProntuarios')