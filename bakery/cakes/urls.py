from django.urls import path, include

from .views import HomePageView, OrderView

from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('form', OrderView, basename='form')


app_name = 'cakes'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
