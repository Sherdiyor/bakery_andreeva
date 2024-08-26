from django.views.generic.base import TemplateView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView
from rest_framework.mixins import CreateModelMixin
from .serializers import CakeSerializer, OrderSerializer
from rest_framework.status import HTTP_201_CREATED
from rest_framework.response import Response
from .models import Order, Cake
from .pagination import CustomPagination


class HomePageView(TemplateView, ListCreateAPIView):
    template_name = "index.html"


class OrderView(ModelViewSet, CreateModelMixin):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)


class BaseCatalogView(ModelViewSet):
    serializer_class = CakeSerializer


class CatalogView(BaseCatalogView):
    queryset = Cake.objects.filter(saled=False)[3:]
    pagination_class = CustomPagination


class HotsView(BaseCatalogView):
    queryset = Cake.objects.all()[:3]
