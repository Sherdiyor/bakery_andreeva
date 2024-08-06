from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Order(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    phone = PhoneNumberField(null=False, blank=False)
    text = models.TextField(null=False, blank=False)


class Cake(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    image = models.ImageField(upload_to='media/')
