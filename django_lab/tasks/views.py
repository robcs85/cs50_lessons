from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django import forms

# Criando variavel global com a lista
# Variavel glocal TAREFAS será chamada posteriormente na função def add()
# ATUALIZAÇÃO -----------> Removendo a variavel global para dentro de def index() para não ser mais acessível
# por todos que acessarem a aplicação visualizar os mesmos dados inseridos no formulário na tarefas[]
#tarefas = ["Django","Python", "JS"]

# - Criando Classe formulário e inserindo os campos de caracteres
class NewTaskForm(forms.Form):
    task = forms.CharField(label="Nova Tarefa")
    #prioridade = forms.IntegerField(label="Prioridade", min_value=1, max_value=5)
    # Novo campo do formulario, inteiro definido valor minimo e maximo
    # Isso faz com que interaja com cliente, obrigando o mesmo a inserir um numero dentro dentro do campo desejado

#------------------------------------------------------------------------------------------------------------#
"""
    1. return render irá renderizar templates chamando através do parametro request o index.html;
    2. A função index, precisa acessar a lista de tarefas criadas na variavel global, e dentro do
    APP "tasks": o que tiver na lista tarefas, mostre o que estiver dentro da lista, que posteriormente será
    chamado em index.html acessando os dados contidos na função definida index
"""
#------------------------------------------------------------------------------------------------------------#
# ATUALIZAÇÃO APÓS REMOVER A VARIAVEL GLOBAL TAREFAS linhas 32, 33, 35
# Checando se existe uma lista de tarefas, se não existe tarefas na sessao, então request.session cria uma lista
# vazia de tarefas para a sessão
#------------------------------------------------------------------------------------------------------------#
def index(request):
    if "tarefas" not in request.session:
        request.session["tarefas"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tarefas"]
    })
#------------------------------------------------------------------------------------------------------------#
# - Adicionando uma nova função que irá renderizar uma nova página chamada add.html
# - Quando for renderizar a pagina tasks html, através da variavel criada form: irá chamar o método que cria
# - o formulario automático sem precisar preencher manualmente como foi feito anteriormente na página add.html
#------------------------------------------------------------------------------------------------------------#
# VALIDACAO DE DADOS COM IF #
#------------------------------------------------------------------------------------------------------------#
# if request.method == "POST": Se o parametro request for igual a POST
# form = NewTaskForm(request.POST) Cria um novo formulario com dados armazenados que o usuario enviou para o
# formuladio, armazenando na variavel form.
# if form.is_valid(): Se o formulario for validado com os dados
# task = form.cleaned_data["task"] Limpe os dados dentro do formulario NewTaskForm() da variavel task
# para uma nova inserção.
# tarefas.append(task) Adiciona dentro da lista tarefas, sendo ela a variavel global contendo a lista[]
# Essa lista e temporária, volatil, ao fechar o SERVER apagará o que foi inserido
# --------------------ATUALIZAÇÃO-----------------> Linhas 64, 65 ----------------------------------->
# Após adicionar as informacoes adicionadas na lista append, quero que redirecione para a pagina tasks
# Adiciono então um retorno utilizando metodo django HttpResponseRedirect("/tasks") ao invés de fazer redirecionamento
# dentro da aplicação para o html, utilizo o metodo reverse, para qualquer pagina index dentro de tasks da função django
# reverse"tasks:index" faça o redirecionamento reverso pocurando esse index da aplicação tasks.
# append(task) agora mudou para += [task]
#------------------------------------------------------------------------------------------------------------#
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tarefas"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        # Mas, se os dados não forem validados acima, entao se não se
        else:
            return render(request, "tasks/add.html",{
                "form": form
            })
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
        })
#  Código acima do else, se os dados não forem validados, reenderiza a pagina html add novamente
#  no entanto, ao inves de retornar a página formualario padrão em branco, retorna com dados na tela erros
#  caso se deparar com algum
