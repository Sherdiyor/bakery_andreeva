from django.shortcuts import render

from .models import Cake
from .forms import OrderForm


def index(request):
    template = 'index.html'
    cakes = Cake.objects.all()
    form = OrderForm(request.POST or None)
    context = {'cakes': cakes, 'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return render(request, template, context)
    return render(request, template, context)
