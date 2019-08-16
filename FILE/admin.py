from django.contrib import admin

# Register your models here.
from .models import UploadFileForm

# Create your models here.

class File(admin.ModelAdmin):
    list_display = ('title',)
    

admin.site.register(UploadFileForm,File)