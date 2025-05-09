"""
Para projetar classes de forma eficaz, você precisa entender como a herança e o polimorfismo funcionam juntos.

Neste exercício, você tem três classes (uma principal e duas secundárias) e cada uma delas tem um método talk().
Analise o código a seguir:

class Parent:
    def talk(self):
        print("Pai falando!")     

class Child(Parent):
    def talk(self):
        print("Criança falando!")          

class TalkativeChild(Parent):
    def talk(self):
        print("TalkativeChild falando!")
        Parent.talk(self)

p, c, tc = Parent(), Child(), TalkativeChild()
for obj in (p, c, tc):
    obj.talk()

Qual é o resultado do código acima?
"""

# resposta 4:
# Pai falando!
# Criança falando!
# TalkativeChild falando!
# Pai falando!
