from django.shortcuts import render
from django.http import HttpResponse
from . models import Numeros


def index(request):
    text = 'Nao sei'
    numeros = Numeros.objects.all()
    context = {'text' : text, 'numeros': numeros}
    return render(request, 'treino/index.html', context)
