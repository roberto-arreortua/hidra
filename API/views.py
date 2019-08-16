from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ConfigSerilizer, HeadSerializer
from .models import Config, Head
from rest_framework import generics
from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404
import os
from django.conf import settings
from django.http import HttpResponse, Http404

# Create your views here.

class ConfigViewSet(viewsets.ModelViewSet):
    #queryset = Config.objects.all()
    queryset = Config.objects.filter(published=False)
    serializer_class = ConfigSerilizer


class HeadStatus(viewsets.ModelViewSet):
    #queryset = Config.objects.all()
    queryset = Head.objects.all()
    serializer_class = HeadSerializer


class HeadConfig(generics.ListCreateAPIView):
    def get_queryset(self):
        print(self.kwargs["pk"])
        queryset = Config.objects.filter(head_id = self.kwargs["pk"])#, agregar and fecha_publicacion > timezone.now()
        return queryset
    serializer_class = ConfigSerilizer



def download_file(request,id):
    print(id)
    try:
        archivo = get_object_or_404(Config, id=id)
        contents = archivo.file
        name_file = archivo.version
        response = HttpResponse(contents)

        response['Content-Disposition'] = 'attachment; filename={}'.format(name_file)

        return response

    except Exception as e:
        if type(e) is Http404:
            return Response(False, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    