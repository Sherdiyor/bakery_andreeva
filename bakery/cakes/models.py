from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Order(models.Model):
    name = models.CharField(
        max_length=50, null=False, blank=False, help_text='имя заказчика'
    )
    phone = PhoneNumberField(
        null=False, blank=False, help_text='телефон заказчика'
    )
    comment = models.TextField(
        null=False, blank=False, help_text='коментарий заказчика'
    )


class Cake(models.Model):
    name = models.CharField(
        max_length=50, null=False, blank=False, help_text='название торта'
    )
    image = models.ImageField(
        upload_to='media/', help_text='фото торта'
    )
    description = models.TextField(
        max_length=70, null=False, blank=False, help_text='описание торта'
    )
    price = models.IntegerField(
        null=False, blank=False, help_text='цена торта'
    )
    weight = models.IntegerField(
        null=False, blank=False, help_text='масса в граммах'
    )
    saled = models.BooleanField(
        blank=False, default=False, help_text='продан'
    )
