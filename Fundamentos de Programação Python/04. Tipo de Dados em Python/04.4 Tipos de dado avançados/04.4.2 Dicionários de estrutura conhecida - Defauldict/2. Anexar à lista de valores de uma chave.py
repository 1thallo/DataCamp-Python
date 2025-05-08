"""
Como anexar à lista de valores de uma chave

Muitas vezes, ao trabalhar com dicionários, você precisará inicializar um tipo de dados antes de poder usá-lo. 
Um ótimo exemplo disso é uma lista, que precisa ser inicializada em cada chave antes que você possa acrescentar algo a essa lista.

Um defaultdict permite que você defina o que cada chave não inicializada conterá. 
Ao estabelecer um defaultdict, você passa para ele o tipo que deseja que ele seja, como list, tuple, set, int, string, dictionary ou qualquer outro objeto de tipo válido.

Você trabalhará com o mesmo registro de peso do último exercício, mas com os pinguins machos do nosso estudo.
"""

# --- Código abaixo ---

# Import defaultdict
from collections import defaultdict

# Create a defaultdict with a default type of list: male_penguin_weights
male_penguin_weights = defaultdict(list)

# Iterate over the weight_log entries
for species, sex, body_mass in weight_log:
    # Use the species as the key, and append the body_mass to it
    male_penguin_weights[species].append(body_mass)
    
# Print the first 2 items of the male_penguin_weights dictionary
print(list(male_penguin_weights.items())[:2])