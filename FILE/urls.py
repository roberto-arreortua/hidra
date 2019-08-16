from django.urls import path 
from .views import File, download, download_file
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('v1', File, base_name='file')


urlpatterns = [
   # path('v1/<slug>', download,name='download' ),
   path('v2/<int:id>', download_file,name='download_file' ),
]

urlpatterns += router.urls
