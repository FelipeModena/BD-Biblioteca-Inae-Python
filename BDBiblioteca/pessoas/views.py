from django.shortcuts import render
from django.http import HttpResponse
from pessoas import queryPessoas

# Create your views here.
def pessoas(request):
    a=queryPessoas.ordemAlfDNomeCadastro("pessoNome1")
    return HttpResponse(a)