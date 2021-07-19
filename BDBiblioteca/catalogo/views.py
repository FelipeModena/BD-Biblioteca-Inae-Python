from typing import List
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from catalogo import queryLivro

# Create your views here.
def helloWorld(request):
    a=queryLivro.ordemAlfAutor("Esopo")
    return HttpResponse(a)