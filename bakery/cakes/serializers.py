from rest_framework.serializers import ModelSerializer
from .models import Order, Cake


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "name",
            "phone",
            "comment",
        )


class CakeSerializer(ModelSerializer):
    class Meta:
        model = Cake
        fields = (
            "name",
            "image",
            "description",
            "price",
            "weight",
            "saled",
        )
