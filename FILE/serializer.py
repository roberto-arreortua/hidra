from rest_framework import serializers
from .models import UploadFileForm



class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadFileForm
        fields = '__all__'