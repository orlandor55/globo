# Generated by Django 3.2.9 on 2021-11-07 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plandectas', '0002_auto_20211107_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='CtasContable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=15, unique=True, verbose_name='Código Contable')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripción de Cta')),
                ('grupo', models.CharField(choices=[('0', 'ACTIVO'), ('1', 'PASIVO'), ('2', 'PATRIMONIO'), ('3', 'RESULTADOS')], max_length=15, verbose_name='Grupo')),
                ('subgrupo', models.CharField(choices=[('0', 'ACTIVO CORRIENTE'), ('1', 'ACTIVO NO CORRIENTE'), ('2', 'PASIVO CORRIENTE'), ('3', 'PASIVO NO CORRIENTE'), ('4', 'RESULTADOS DEL EJERCICIO')], max_length=25, verbose_name='Sub-Grupo')),
                ('rubro', models.CharField(max_length=25, verbose_name='Rubro')),
                ('subrubro', models.CharField(max_length=50, verbose_name='Sub-rubro')),
                ('monetario', models.CharField(choices=[('0', 'M'), ('1', 'NM')], max_length=2, verbose_name='Monetario/No Monetario')),
                ('nombre_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plandectas.empresasclientes')),
            ],
            options={
                'verbose_name': 'Plan de Cuenta',
                'verbose_name_plural': 'Códigos de Cuentas',
            },
        ),
        migrations.CreateModel(
            name='SumasYSaldos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes_inicio', models.FloatField(blank=True, verbose_name='Mes de Inicio')),
                ('cierre_anterior', models.CharField(max_length=10, verbose_name='Mes de Cierre Anterior')),
                ('axi_ejercicio_anterior', models.FloatField(blank=True, default=0, verbose_name='Ajuste por Inflación Inicial')),
                ('mes1', models.FloatField(blank=True, verbose_name='Mes 1')),
                ('mes2', models.FloatField(blank=True, verbose_name='Mes 2')),
                ('mes3', models.FloatField(blank=True, verbose_name='Mes 3')),
                ('mes4', models.FloatField(blank=True, verbose_name='Mes 4')),
                ('mes5', models.FloatField(blank=True, verbose_name='Mes 5')),
                ('mes6', models.FloatField(blank=True, verbose_name='Mes 6')),
                ('mes7', models.FloatField(blank=True, verbose_name='Mes 7')),
                ('mes8', models.FloatField(blank=True, verbose_name='Mes 8')),
                ('mes9', models.FloatField(blank=True, verbose_name='Mes 9')),
                ('mes10', models.FloatField(blank=True, verbose_name='Mes 10')),
                ('mes11', models.FloatField(blank=True, verbose_name='Mes 11')),
                ('mes12', models.FloatField(blank=True, verbose_name='Mes 12')),
                ('mes13', models.FloatField(blank=True, default=0, verbose_name='Mes 13')),
                ('cierre', models.CharField(max_length=10, verbose_name='Mes de Reporte')),
                ('codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plandectas.ctascontable')),
            ],
            options={
                'verbose_name': 'Sumas Y Saldos',
                'verbose_name_plural': 'Sumas Y Saldos',
            },
        ),
    ]
