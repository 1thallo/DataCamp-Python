"""
Manipulação de listas para diversão e lucro

Você já deve saber como adicionar elementos de dados individuais a uma lista usando o método .append().

No entanto, se você quiser combinar uma lista com outro tipo de matriz (lista, conjunto, tupla), você
pode usar o método .extend() na lista.

Você também pode usar o método .index() para encontrar a posição de um item em uma lista. Em seguida, você pode usar essa posição para remover o item com o método .pop().

Neste exercício, você praticará o uso de todos esses métodos!
"""

# --- Código abaixo ---

# Create a list containing the names: baby_names
baby_names = ['Ximena', 'Aliza', 'Ayden', 'Calvin']

# Extend baby_names with 'Rowen' and 'Sandeep'
baby_names.extend(['Rowen', 'Sandeep'])

# Find the position of 'Rowen': position
position = baby_names.index('Rowen')

# Remove 'Rowen' from baby_names
baby_names.pop(position)

# Print baby_names
print(baby_names)