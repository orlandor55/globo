from django.db import models
from aplications.plandectas.models import (
    EmpresasClientes,
    CtasContable,
)

# Create your models here.



class ActivosFijos(models.Model):
    empresa = models.ForeignKey(EmpresasClientes, on_delete=models.CASCADE, blank=True)
    descripcion = models.CharField('Descripción', max_length=50)
    #cliente = models.ForeignKey(OTHERMODEL, on_delete=models.CASCADE)
    #user_creator = models.ForeignKey(OTHERMODEL, on_delete=models.CASCADE)
    codigo_cta = models.ForeignKey(CtasContable, on_delete=models.CASCADE)
    mes_adquisicion = models.CharField('Mes de Adquisición/Origen', max_length=2) 
    ano_adquisicion = models.CharField('Año de Adquisición/Origen', max_length=4) 
    valor_origen = models.FloatField()
    vida_util = models.IntegerField()
    cta_contable_amort_acum = models.ForeignKey(
        CtasContable, 
        on_delete=models.CASCADE, 
        related_name='cta_AA'
    )
    amort_acum = models.FloatField()
    cta_contable_amort_ejercicio = models.ForeignKey(
        CtasContable, 
        on_delete=models.CASCADE, 
        related_name='cta_AE'
    )
    amort_ejercicio = models.FloatField()

    class Meta:
        verbose_name = 'Activo Fijo'
        verbose_name_plural = 'Activos Fijos'

    def __str__(self):
        return self.descripcion
