# Generated by Django 3.2.9 on 2021-11-04 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plandectas', '0002_auto_20211103_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sumasysaldos',
            name='cierre_anterior',
            field=models.CharField(max_length=10, verbose_name='Mes de Cierre Anterior'),
        ),
    ]