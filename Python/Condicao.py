# Condicoes if, elif, else

# variavel numero irá receber os dados que o usuario digitou e irá armazena-la
# a função int. converte o numero string digitado pelo usuario em input para numero inteiro
numero = int(input("Entre com um numero: "))

# condicao ira avaliar se este numero e positivo, negativo ou zero
if (numero > 0):
    print(f" O valor {numero} é positivo")
elif (numero < 0):
    print(f" O valor {numero} é negativo")
else:
    print(" o valor e zero ")