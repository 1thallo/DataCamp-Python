"""
Como encontrar os elementos mais comuns

Outro uso poderoso do Counter é encontrar os elementos mais comuns em uma lista. 
Isso pode ser feito com o método .most_common().

Pratique o uso dessa ferramenta agora para encontrar as espécies mais comuns em uma lista de pinguins.
"""

# --- Código abaixo ---

# Import the Counter object
from collections import Counter

# Create a Counter of the penguins list: penguins_species_counts
penguins_species_counts = Counter(penguin["Species"] for penguin in penguins)

# Find the 3 most common species counts
print(penguins_species_counts.most_common(3))