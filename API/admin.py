from django.contrib import admin

# Register your models here.
from .models import  Head, Config
# Register your models here.

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('name',)
    

class CampaingAdmin(admin.ModelAdmin):
    list_display = ('name',)
    

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('name',)
   

class HeadAdmin(admin.ModelAdmin):
    list_display = ('name',)
   

class ConfigAdmin(admin.ModelAdmin):
    list_display = ('version',)
    




admin.site.register(Head,HeadAdmin)
admin.site.register(Config,ConfigAdmin)