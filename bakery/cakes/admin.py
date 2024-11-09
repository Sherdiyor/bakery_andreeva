from django.contrib import admin

from .models import Order, Cake, Contacts


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'phone',
        'comment',
    ]
    search_fields = [
        'name',
    ]


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'image',
        'description',
        'price',
    ]
    search_fields = [
        'name',
    ]


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = [
        'tel',
        'telegram',
        'instagram',
        'address'
    ]
