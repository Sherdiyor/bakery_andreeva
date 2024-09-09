from django.urls import path, include

from .views import HomePageView, OrderView, CatalogView, HotsView

from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('form', OrderView, basename='form')
router.register(r'catalog', CatalogView, basename='catalog')
router.register('hots', HotsView, basename='hots')


app_name = 'cakes'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
