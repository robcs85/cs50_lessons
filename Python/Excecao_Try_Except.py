import sys
"""
    Importando a biblioteca para executar a ação de sair ao acontecer o erro
    Solicitando ao usuario inserir dados numericos, em caso do usuario digitar strings.
    Acontecerá o tratamento de exceção, fazendo com que saio do programa e imprima a mensagem dizendo o porque encerrou
"""
try:
    X = int(input("Digite um numero divisor para X: "))
    Y = int(input("Ddigite um numero divisor por Y: "))
except ValueError:
    print("Erro: Digite apenas numeros inteiros. ")
    sys.exit(1)
"""
    Tente fazer a divisão, em caso do usuario entrar com valor zero na divisão, e aconteça o 
    erro ZeroDivisionError, mostre o erro e saia do programa sys.exit(') faz encerrar o programa
"""

try:
    resultado = X / Y
except ZeroDivisionError:
    print("Erro: Não pode ser divido por zero")
    sys.exit(1)

print(f" O valor {X} dividido por {Y} é igual a: {resultado}")