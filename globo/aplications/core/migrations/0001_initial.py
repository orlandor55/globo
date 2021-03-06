# Generated by Django 3.2.9 on 2021-11-03 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CtasContable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=15, verbose_name='Código Contable')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripción de Cta')),
                ('grupo', models.CharField(max_length=15, verbose_name='Grupo')),
                ('subgrupo', models.CharField(max_length=25, verbose_name='Sub-Grupo')),
                ('rubro', models.CharField(max_length=25, verbose_name='Rubro')),
                ('subrubro', models.CharField(max_length=50, verbose_name='Sub-rubro')),
                ('monetario', models.CharField(choices=[('0', 'M'), ('1', 'NM')], max_length=2, verbose_name='Monetario/No Monetario')),
            ],
            options={
                'verbose_name': 'Plan de Cuenta',
                'verbose_name_plural': 'Planes de Cuentas',
            },
        ),
    ]
