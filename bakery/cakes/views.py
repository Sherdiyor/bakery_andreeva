from django.shortcuts import render
from .models import Cake


def index(request):
    template = 'index.html'
    cakes = Cake.objects.all()
    context = {'cakes': cakes}
    return render(request, template, context)
