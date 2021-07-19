from django.shortcuts import render
from django.http import HttpResponse
from emprestimos import queryEmprestimos

# Create your views here.
def emprestimos(request):
    #a=queryEmprestimos.codigoLivro(1)
    return HttpResponse("Hello emprestimos")