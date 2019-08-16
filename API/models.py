from django.db import models
from django.utils import timezone
# Create your models here.

class Head(models.Model):
    name =  models.CharField(verbose_name="Nombre",max_length = 50, unique = True, blank = False)
    ubicacion = models.CharField(verbose_name="Ubicacion", max_length = 100, unique = True, blank = False)
    active = models.BooleanField(verbose_name="Activo",default=False)

    class Meta:
        verbose_name = 'Head(Player)'
        verbose_name_plural = 'Heads(Player)'
        ordering = ['-name']
    def __str__(self):
        return self.name


class Config(models.Model):
    version = models.CharField(max_length = 50, unique = True, blank = False )
    fecha_publicacion = models.DateField( blank = False)
    fecha_despublicacion = models.DateField(blank = False)
    priority = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    lunes_inicio = models.TimeField(blank = True, default= None, null = True)
    lunes_fin = models.TimeField(blank = True, default= None, null = True)
    martes_inicio = models.TimeField(blank = True, default= None, null = True)
    martes_fin = models.TimeField(blank = True, default= None, null = True)
    miercoles_inicio = models.TimeField(blank = True, default= None, null = True)
    miercoles_fin = models.TimeField(blank = True, default= None, null = True)
    jueves_inicio = models.TimeField(blank = True, default= None, null = True)
    jueves_fin = models.TimeField(blank = True, default= None, null = True)
    viernes_inicio = models.TimeField(blank = True, default= None, null = True)
    viernes_fin = models.TimeField(blank = True, default= None, null = True)
    sabado_inicio = models.TimeField(blank = True, default= None, null = True)
    sabado_fin = models.TimeField(blank = True, default= None, null = True)
    domingo_inicio = models.TimeField(blank = True, default= None, null = True)
    domingo_fin = models.TimeField(blank = True, default= None, null = True)
    head = models.ForeignKey(Head, on_delete=models.CASCADE)
    file = models.FileField(upload_to="Hidra", default = None, null = True, blank = True)

    class Meta:
        verbose_name = 'Configuracion'
        verbose_name_plural = 'Configuraciones'
        ordering = ['-fecha_publicacion']

    def __int__(self):
        return self.version
