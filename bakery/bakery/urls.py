from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken import views


urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    # path('api/auth/', include('djoser.urls.authtoken')),
    # path('api/auth/', include('djoser.urls.jwt')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('admin/', admin.site.urls),
    path('', include('cakes.urls', namespace='cakes')),
]
