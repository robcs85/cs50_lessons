from django.shortcuts import render
# Criando variavel global com a lista
tarefas = ["Django","Python", "JS"]

#------------------------------------------------------------------------------------------------------------#
"""
    1. return render irá renderizar templates chamando através do parametro request o index.html;
    2. A função index, precisa acessar a lista de tarefas criadas na variavel global, e dentro do
    APP "tasks": o que tiver na lista tarefas, mostre o que estiver dentro da lista, que posteriormente será
    chamado em index.html acessando os dados contidos na função definida index
"""
#------------------------------------------------------------------------------------------------------------#
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tarefas
    })