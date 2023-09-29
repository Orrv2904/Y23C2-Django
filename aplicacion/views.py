from django.shortcuts import render
from .models import Hackaton

def index(request):
    modelo = Hackaton.objects.all()
    contexto = {
        "modelo": modelo,
    }
    return render(request, "index.html", contexto)
