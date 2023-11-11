# Função SET() vazia
FuncaoSet = set()
# adicionando elementos a função SET
# Como percebido na primeira execução, set() ele não repete elementos como e o caso do 2 adicionados 2 vezes
FuncaoSet.add(1)
FuncaoSet.add(2)
FuncaoSet.add(3)
FuncaoSet.add(4)
FuncaoSet.add(2)
FuncaoSet.add(8)

FuncaoSet.remove(2) # remove no caso, os dois elementos contendo 2
print(FuncaoSet)
# função len() verifica quantos elementos tem dentro da função set()
print(f" Há {len(FuncaoSet)} elementos dentro da função set() ")