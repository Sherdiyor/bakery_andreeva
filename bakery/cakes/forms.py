from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = {
            'name',
            'phone',
            'text',
        }
        lables = {
            'name': 'Введите ваше имя',
            'phone': 'Введите номер телефона',
            'text': 'Введите описание вашего заказа',
        }
