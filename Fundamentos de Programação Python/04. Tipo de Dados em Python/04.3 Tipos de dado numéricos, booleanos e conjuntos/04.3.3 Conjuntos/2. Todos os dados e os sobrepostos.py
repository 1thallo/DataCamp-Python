"""
Encontrar todos os dados e os dados sobrepostos entre os conjuntos

Os conjuntos têm vários métodos para combinar, comparar e estudar todos eles com base na teoria dos conjuntos. 
O método .union() retorna um conjunto de todos os elementos encontrados no conjunto que você usou o método, 
além de todos os conjuntos passados como argumentos para o método. 
Você também pode procurar por dados sobrepostos em conjuntos, usando o método .intersection() em um conjunto e passando outro conjunto como argumento. 
Ele retornará um conjunto vazio se não houver correspondência.

Sua tarefa neste exercício é encontrar a união e a interseção nas espécies de pinguins machos e fêmeas. 
Para isso, dois conjuntos foram pré-carregados em seu espaço de trabalho: female_penguin_species e male_penguin_species.
"""

# --- Código abaixo ---

# Find the union: all_species
all_species = female_penguin_species.union(male_penguin_species)

# Print the count of names in all_species
print(len(all_species))

# Find the intersection: overlapping_species
overlapping_species = female_penguin_species.intersection(male_penguin_species)

# Print the count of species in overlapping_species
print(len(overlapping_species))