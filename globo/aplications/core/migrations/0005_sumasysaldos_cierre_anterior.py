# Generated by Django 3.2.9 on 2021-11-03 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20211103_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='sumasysaldos',
            name='cierre_anterior',
            field=models.CharField(default=0, max_length=10, verbose_name='Cierre Anterior'),
        ),
    ]
