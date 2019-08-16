from django.db import models
from django import forms

class UploadFileForm(models.Model):
    title = models.CharField(max_length=50, unique = True, blank = False)
    file = models.FileField(upload_to="Hidra")



    class Meta:
        verbose_name = 'Archivo'
        verbose_name_plural = 'Archivos'
        ordering = ['-title']
    def __str__(self):
        return self.title