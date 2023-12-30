from django.urls import path
from . import views

# a URL que será chamada no navegador. apontando para views que contem a função definida index com o retorno
# da lista de tarefas
# Quando digitar tasks/add será chamada essa função add() dentro de views

# Noemeando os nome das paginas dos app ADD e index para serem chamadas por TASKS, para não haver colisão com outras
# paginas index de outros projetos
app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]