from django.db import models

# Create your models here.
class CtasContable(models.Model):
    MONETARIO_NO_MONETARIO = (
        ('0', 'M'),
        ('1', 'NM'),
    )
    GRUPO = (
            ('0', 'ACTIVO'),
            ('1', 'PASIVO'),
            ('2', 'PATRIMONIO'),
            ('3', 'RESULTADOS'),
    )
    SUB_GRUPO = (
            ('0', 'ACTIVO CORRIENTE'),
            ('1', 'ACTIVO NO CORRIENTE'),
            ('2', 'PASIVO CORRIENTE'),
            ('3', 'PASIVO NO CORRIENTE'),
            ('4', 'RESULTADOS DEL EJERCICIO'),
    )

    empresa = models.CharField('Cliente', max_length=50)
    codigo = models.CharField('Código Contable', max_length=15)
    descripcion = models.CharField('Descripción de Cta', max_length=50)
    grupo = models.CharField('Grupo', max_length=15, choices=GRUPO)
    subgrupo = models.CharField('Sub-Grupo', max_length=25, choices=SUB_GRUPO)
    rubro = models.CharField('Rubro', max_length=25)
    subrubro = models.CharField('Sub-rubro', max_length=50)
    monetario = models.CharField('Monetario/No Monetario', max_length=2, choices=MONETARIO_NO_MONETARIO)
    #cta_relacionada = models.ForeignKey(OTHERMODEL, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Plan de Cuenta'
        verbose_name_plural = 'Códigos de Cuentas'

    def __str__(self):
        return self.codigo + ' - ' + self.subrubro


class SumasYSaldos(models.Model):
    codigo = models.ForeignKey(
        CtasContable, 
        on_delete=models.CASCADE)
    mes_inicio = models.FloatField(
        'Mes de Inicio', 
        blank=True)
    cierre_anterior = models.FloatField(
        'Cierre Anterior',
        default=0
        )
    axi_ejercicio_anterior = models.FloatField(
        'Ajuste por Inflación Inicial', 
        blank=True,
        default=0)
    mes1 = models.FloatField('Mes 1', blank=True)
    mes2 = models.FloatField('Mes 2', blank=True)
    mes3 = models.FloatField('Mes 3', blank=True)
    mes4 = models.FloatField('Mes 4', blank=True)
    mes5 = models.FloatField('Mes 5', blank=True)
    mes6 = models.FloatField('Mes 6', blank=True)
    mes7 = models.FloatField('Mes 7', blank=True)
    mes8 = models.FloatField('Mes 8', blank=True)
    mes9 = models.FloatField('Mes 9', blank=True)
    mes10 = models.FloatField('Mes 10', blank=True)
    mes11 = models.FloatField('Mes 11', blank=True)
    mes12 = models.FloatField('Mes 12', blank=True)
    mes13 = models.FloatField('Mes 13', blank=True, default=0)
    cierre = models.CharField(
        'Mes de Reporte',
        max_length=10
        )

    class Meta:
        verbose_name = 'Sumas Y Saldos'
        verbose_name_plural = 'Sumas Y Saldos'

    def __str__(self):
        return 'Sumas y Saldos a ' + self.cierre

