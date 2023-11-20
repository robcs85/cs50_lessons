# importando bibliotecas django para que torne possível ação da pagina
# Para que a url seja visível, importa caminho da url criada dentro de hello

from django.urls import path
from . import views

# Chamando a função greet, e qualquer nome que usuario digitar após hello/
# irá passar ao parâmetro nome, trazendo na tela Olá, Fulano
# Qualquer coisa digitara no caminho após hello/ o parametro nome dentro da função greet irá trazer em tela
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:nome>", views.greet, name="greet"),
    path("rob", views.rob, name="rob"),
    path("bob", views.bob, name="bob")
]