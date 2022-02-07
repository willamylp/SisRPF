from django.db import models
from datetime import datetime

# Create your models here.
class Prontuario(models.Model):
    numero = models.CharField(max_length=10, blank=False)
    data = models.DateField(blank=False)
    unidade_saude = models.CharField(max_length=100, blank=False, default='HMTLQS')
    class Meta:
        verbose_name = ("Prontuario Familiar")
        verbose_name_plural = ("Prontuarios")

    def __str__(self):
        return '{} / {}'.format(self.numero, self.ano)

    def get_absolute_url(self):
        return reverse("Prontuario_detail", kwargs={"pk": self.pk})

class Responsavel(models.Model):
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
    # ---> INFORMAÇÕES PESSOAIS <---
    nome = models.CharField(max_length=200, blank=False, null=False)
    dt_nascimento = models.DateField(blank=False)
    cpf = models.CharField(max_length=14, unique=True, blank=True, null=True)

    # ---> ENDEREÇO <---
    logradouro = models.CharField(max_length=100, blank=False)
    num_endereco = models.CharField(max_length=10, blank=False)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=False)
    ponto_referencia = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = ("Responsavel")
        verbose_name_plural = ("Responsaveis")

    def __str__(self):
        return '{} | {}/{}'.format(self.nome, self.prontuario.numero, self.prontuario.ano)

    def get_absolute_url(self):
        return reverse("Responsavel_detail", kwargs={"pk": self.pk})

class GrupoFamiliar(models.Model):

    SEXO = (
        ('Feminino', 'FEMININO'),
        ('Masculino', 'MASCULINO'),
        ('Ignorado', 'IGNORADO')
    )
    ESTADO_CIVIL = (
        ('Casado(a)', 'CASADO(A)'),
        ('Divorciado(a)', 'DIVORCIADO(A)'),
        ('Separado(a)', 'SEPARADO(A)'),
        ('Solteiro(a)', 'SOLTEIRO(A)'),
        ('União Estável(a)', 'UNIÃO ESTÁVEL(A)'),
        ('Viúvo(a)', 'VIÚVO(A)'),
        ('Outro', 'OUTRO')
    )
    ESCOLARIDADE = (
        ('Abalfabeto', 'ANALFABETO'),
        ('Fundamental Incompleto', 'FUNDAMENTAL INCOMPLETO'),
        ('Fundamental Completo', 'FUNDAMENTAL COMPLETO'),
        ('Médio Incompleto', 'MÉDIO INCOMPLETO'),
        ('Médio Completo', 'MÉDIO COMPLETO'),
        ('Superior Incompleto', 'SUPERIOR INCOMPLETO'),
        ('Superior Completo', 'SUPERIOR COMPLETO'),
        ('Pós-graduação Incompleto', 'PÓS-GRADUAÇÃO INCOMPLETO'),
        ('Pós-graduação Completo', 'PÓS-GRADUAÇÃO COMPLETO'),
    )

    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)

    nome = models.CharField(max_length=200, blank=False, null=False)
    parentesco = models.CharField(max_length=50, blank=False, null=False)
    dt_nascimento = models.DateField(blank=False)

    sexo = models.CharField(max_length=20, blank=True, choices=SEXO, default='')
    estado_civil = models.CharField(max_length=50, blank=True, choices=ESTADO_CIVIL, default='')
    naturalidade = models.CharField(max_length=20, blank=False, null=False)
    escolaridade = models.CharField(max_length=50, blank=True, choices=ESCOLARIDADE, default='')
    ativ_economica = models.CharField(max_length=50, blank=False, null=False)
    renda = models.FloatField(blank=True)

    class Meta:
        verbose_name = ("Grupo Familiar")
        verbose_name_plural = ("GruposFamiliares")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("GrupoFamiliar_detail", kwargs={"pk": self.pk})
