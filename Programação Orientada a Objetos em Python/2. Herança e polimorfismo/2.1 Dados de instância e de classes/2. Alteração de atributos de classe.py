"""
Instruções 1/2

Crie dois objetos Player, p1 e p2.
Imprima p1.MAX_SPEED e p2.MAX_SPEED.
Atribua 7 a p1.MAX_SPEED.
Imprima p1.MAX_SPEED e p2.MAX_SPEED novamente.
Imprima Player.MAX_SPEED.
Examine o resultado cuidadosamente.
"""

# -- Código 1 --

# Create Players p1 and p2
p1 = Player()
p2 = Player()

print("MAX_SPEED of p1 and p2 before assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

# Assign 7 to p1.MAX_SPEED
p1.MAX_SPEED = 7

print("MAX_SPEED of p1 and p2 after assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

print("MAX_SPEED of Player:")
# Print Player.MAX_SPEED
print(Player.MAX_SPEED)

"""
Instruções 2/2

Modifique a atribuição para atribuir 7 a Player.MAX_SPEED em vez de p1.MAX_SPEED.
Imprima p1.MAX_SPEED, p2.MAX_SPEED e Player.MAX_SPEED para confirmar que todos refletem a mudança.
"""

# -- Código 2 --

# Create Players p1 and p2
p1, p2 = Player(), Player()

print("MAX_SPEED of p1 and p2 before assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

# ---MODIFY THIS LINE--- 
Player.MAX_SPEED = 7

print("MAX_SPEED of p1 and p2 after assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

print("MAX_SPEED of Player:")
# Print Player.MAX_SPEED
print(Player.MAX_SPEED)
