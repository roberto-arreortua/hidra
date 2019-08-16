from django.urls import path 
from .views import ConfigViewSet, HeadStatus, HeadConfig, download_file
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('v1/config', ConfigViewSet, base_name='config')
router.register('v1/head', HeadStatus, base_name='head')

urlpatterns = [
    path('v1/head/<int:pk>/config/', HeadConfig.as_view(),name='configuraciones'),
    path('v1/file/<int:id>', download_file,name='download_file' ),
]

urlpatterns += router.urls
