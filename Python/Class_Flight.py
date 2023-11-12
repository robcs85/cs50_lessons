class Flight():
    # Definindo metodos construtor com a capacidade total de vagas na aeronave e de passageiros para a mesma
    # Inicia uma lista de passageiros vazia []
    def __init__(self, capacidade):
        self.capacity = capacidade
        self.passengers = []

        # Definindo método passageiros para adicionar passageiros pelo nome na lista passageiros[]
        # Self para acessar a variavel lista de passageiros, self.passengers.append(name)
    def adiciona_passageiro(self, name):
         #Se não há assentos disponiveis, retone Falso
        if not self.assentos_disponiveis():
            return False
        self.passengers.append(name)
        return True
         # Se verdade, continua

        # Como não há um limite de capacidade de assentos por aeronave. O metodo a seguir faz essa verificação
        # Faz a operação de contagem de assentos disponiveis, capacidade - len(self.passangers)
        # capacidade 3 - numeros de pessoas na lista pessoas []
    def assentos_disponiveis(self):
        return self.capacity - len(self.passengers)
# Numero de capacidade (capacity) ao Voo Flight()
voo = Flight(3)

# Criando uma lista com pessoas para serem adicionadas pelo metodo adiciona_passageiros
# Se adicionados passageiros com sucesso, retorna True e imprime, o contrario não haverá mais vagas
pessoas = ["Ross", "Chandler", "Rachel", "Monica"]
for usuario in pessoas:
    if voo.adiciona_passageiro(usuario):
       print(f" Passageiro {usuario} adicionado com sucesso ao Voo. ")
    else:
       print(f"Não há vagas disponiveis para {usuario}")
