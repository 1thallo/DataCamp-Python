"""
Instruções 1/2

Crie uma classe Racer herdada de Player,
Atribua 5 a MAX_SPEED no corpo da classe.
Crie um objeto Player p e um objeto Racer r (não são necessários argumentos para o construtor).
Examine as impressões cuidadosamente.
"""

# -- Código --

# Create a Racer class and set MAX_SPEED to 5
class Racer(Player):
    MAX_SPEED = 5

# Create a Player and a Racer objects
p = Player()
r = Racer()

print("p.MAX_SPEED = ", p.MAX_SPEED)
print("r.MAX_SPEED = ", r.MAX_SPEED)

print("p.MAX_POSITION = ", p.MAX_POSITION)
print("r.MAX_POSITION = ", r.MAX_POSITION)

""" Instruções 2/2

Pergunta
Qual das seguintes afirmações sobre herança de atributos de classe está correta?

Respostas possíveis

Os atributos de classe NÃO PODEM ser herdados, mas novos atributos de classe com o mesmo nome PODEM ser criados em uma classe filha.

Os atributos de classe NÃO PODEM ser herdados, e novos atributos de classe com o mesmo nome NÃO PODEM ser criados em uma classe filha.

X >> Os atributos de classe PODEM ser herdados, e o valor dos atributos de classe PODEM ser substituídos na classe filha

Os atributos de classe podem ser herdados, e o valor dos atributos de classe NÃO PODE ser substituído na classe filha
"""