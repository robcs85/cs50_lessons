# Definindo uma lista com dicionario dentro
pessoas = [
    {"Name": "Ross Geller", "House": "Rua A"},
    {"Name": "Rachel", "House": "Rua B"},
    {"Name": "Chandler", "House": "Rua C"}
]
# Definindo a função Procura_Dictionary para dizer a função sort() abaixo o que ele deve procurar, se por nome
# ou por House
"""
 def Procura_Dictionary(info):
    return info["Name"]
"""
# Ao invés de definir uma função apenas para sort() procurar dentro do dicionario, posso chamar a biblioteca lambda para isso

# Tentativa de ordernar essas pessoas, no entanto, acontecerá um erro de instancias.
# Em python sort() não sabe como comparar os elementos dentro do dicionário {}
# Para isso ocorrer, tenho que dizer a função sort() como fazer, definindo uma outra função antes
# Função sort() olhe para função Procura_Dictionary como palavra chave (key=) e o que estiver dentro, você retorna ordenando-os
pessoas.sort(key=lambda procura: procura["Name"])
# A linha acima esta fazendo a mesma coisa da função definida acima, só que organizada e optimizando código


print(pessoas)