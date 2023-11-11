# Importando a função Multiplica_Valores para multiplicar valores do laço for
from Funcao_Def import Multiplica_Valores

# Criando laço for com range de um a 10
for i in range(10):
    # A cada interação, multiplica o valor por ele mesmo e chama a função definida em square
    # para multiplicar X * X ele por ele mesmo
    print(f" O numero {i} multiplicado por {i}  e igual a {Multiplica_Valores(i)}")
