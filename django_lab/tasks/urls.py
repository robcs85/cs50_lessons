from django.urls import path
from . import views

# a URL que será chamada no navegador. apontando para views que contem a função definida index com o retorno
# da lista de tarefas

urlpatterns = [
    path("", views.index, name="index")
]