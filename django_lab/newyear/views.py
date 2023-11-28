from django.shortcuts import render
import datetime
# Create your views here.
"""
    Definindo a função index que irá fazer uma verificação booleana se é primeiro de janeiro de 2024 ou não
"""
"""
    Função index, compara se é primeiro mês 1 e mês um em uma condição booleana
    Variavel newyear declarada recebe as atribuições booleana, e compara se é dia 1 e mês 1 de 2024, informações 
    fornecidas pela biblioteca datetime que pega as informações atual do sistema.
    A variavel newyear sera chamada em TEMPLATES/NEWYEAR/index.html  
"""
def index(request):
    agora = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": agora.month == 1 and agora.day == 1
    })
