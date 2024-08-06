from django.urls import path

from .views import index

app_name = 'cakes'

urlpatterns = [
    path('', index, name='index')
]
