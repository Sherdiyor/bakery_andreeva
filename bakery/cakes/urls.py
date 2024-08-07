from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import index

app_name = 'cakes'

urlpatterns = [
    path('', index, name='index')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
