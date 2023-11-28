from django.http import HttpResponse
from django.shortcuts import render

"""
# Create your views here.
# funcao inde pega um argumento request que é acessada pelo user, retorna para a página através do argumento passado na função
# uma mensagem.
-------------------------------------------
HttpResponse pertence a django, para usa-lo aqui deve ser importada
Com a importação da função HttpResponse, foi passado uma ação para que o request da função index retorne a mensagem na tela
"""


def index(request):
    return render(request, "hello/index.html")
def rob(request):
    return HttpResponse("Olá, Roberson")
def bob(request):
    return HttpResponse("Ola, Bob")
# Definindo uma função GREET, quando requisitada retornará um nome qualquer digitado pelo usuario, sem precisar
# definir uma função para cada nome como foi feito acima, ao chamar hello/fulano, trasmitirá olá, fulano mesmo que
# não tenha essa função definida. Agora em urls.py defino o caminho de busca
def greet(request, nome):
    return render(request, "hello/greet.html", {
        "nome": nome.capitalize()
    }) #captalize formada primeira letra em maiúscula