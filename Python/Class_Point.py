
# Definindo classe Point()
class Point():
    # Definindo função construtora que será chamada posteriormente
    # input1, input2 os dados dessas variaveis serão repassados para X e Y
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2
p = Point(2, 8)

print(p.x)
print(p.y)
