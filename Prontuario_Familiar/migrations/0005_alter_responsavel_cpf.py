# Generated by Django 4.0.2 on 2022-03-30 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prontuario_Familiar', '0004_rename_nome_grupofamiliar_nome_integrante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsavel',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
    ]