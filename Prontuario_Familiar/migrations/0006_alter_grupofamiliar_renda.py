# Generated by Django 4.0.2 on 2022-03-30 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prontuario_Familiar', '0005_alter_responsavel_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupofamiliar',
            name='renda',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
