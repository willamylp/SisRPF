# Generated by Django 4.0.2 on 2022-02-02 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prontuario_Familiar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupofamiliar',
            name='sexo',
            field=models.CharField(blank=True, choices=[('Feminino', 'FEMININO'), ('Masculino', 'MASCULINO'), ('Ignorado', 'IGNORADO')], default='', max_length=20),
        ),
    ]
