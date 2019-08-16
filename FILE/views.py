from rest_framework import viewsets
from .serializer import FileSerializer
from .models import UploadFileForm
from rest_framework import generics
from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404
# Create your views here.


class File(viewsets.ModelViewSet):
    queryset = UploadFileForm.objects.all()
    serializer_class = FileSerializer
    


import os
from django.conf import settings
from django.http import HttpResponse, Http404

def download(request, path):
    print("-----> ", path)
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type=".zip")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def download_file(request,id):
    print(id)
    
    try:
        archivo = get_object_or_404(UploadFileForm, id=id)
        contents = archivo.file
        name_file = archivo.title
        response = HttpResponse(contents)

        response['Content-Disposition'] = 'attachment; filename={}'.format(name_file)

        return response

    except Exception as e:
        if type(e) is Http404:
            return Response(False, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    