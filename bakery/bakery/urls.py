from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken import views
from .settings import DEBUG


urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),

    path('admin/', admin.site.urls),
    path('', include('cakes.urls', namespace='cakes')),
]

api_routes = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
]

if DEBUG is True:
    urlpatterns + api_routes
