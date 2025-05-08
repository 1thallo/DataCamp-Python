"""
Instruções 1/2

Defina uma classe Player que tenha:
- Um atributo de classe MAX_POSITION com o valor 10;
- O método __init__() que define o atributo de instância position como 0;
- Imprima Player.MAX_POSITION;
- Crie um objeto Player p e imprima seu MAX_POSITION.
"""

# -- Código para Instrução 1 --

class Player:
    MAX_POSITION = 10

    def __init__(self):
        self.position = 0

# Print Player.MAX_POSITION       
print(Player.MAX_POSITION)

# Create a Player object and print its MAX_POSITION
p = Player()
print(p.MAX_POSITION)


"""
Instruções 2/2

Adicione um método move() com um parâmetro steps tal que:
- Se position + steps for menor ou igual a MAX_POSITION, adicione steps a position;
- Caso contrário, defina position como MAX_POSITION;
- Use o método draw() para visualizar no console.
"""

# -- Código para Instrução 2 --

class Player:
    MAX_POSITION = 10

    def __init__(self):
        self.position = 0

    def move(self, steps):
        if self.position + steps <= Player.MAX_POSITION:
            self.position += steps
        else:
            self.position = Player.MAX_POSITION

    def draw(self):
        drawing = "-" * self.position + "|" + "-" * (Player.MAX_POSITION - self.position)
        print(drawing)

# Create player and visualize movement
p = Player(); p.draw()
p.move(4); p.draw()
p.move(5); p.draw()
p.move(3); p.draw()
