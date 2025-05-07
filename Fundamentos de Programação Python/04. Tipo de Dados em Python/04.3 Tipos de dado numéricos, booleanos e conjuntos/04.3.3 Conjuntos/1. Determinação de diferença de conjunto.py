"""
Determinação de diferenças de conjunto

Outra forma de comparar conjuntos é usar o método difference(). Ele retorna todos os itens encontrados em um conjunto, mas não em outro. 
É importante lembrar que o conjunto em que você chamar o método será aquele do qual os itens serão retornados. 
Ao contrário das tuplas, você pode add() itens em um conjunto. Um conjunto só adicionará itens que não existam no conjunto.

Neste exercício, você explorará quais espécies tinham indivíduos do sexo masculino em nossa amostra, mas não tinham indivíduos do sexo feminino. 
O conjunto male_penguin_species foi pré-carregado em seu espaço de trabalho.
"""

# --- Código abaixo ---

# Use a list comprehension to iterate over each penguin in penguins saved as female_species_list
# If the the sex of the penguin is 'FEMALE', return the species value
female_species_list = [penguin["species"] for penguin in penguins if penguin["sex"] == 'FEMALE']

# Create a set using the female_species_list as female_penguin_species
female_penguin_species = set(female_species_list)

# Find the difference between female_penguin_species and male_penguin_species. Store the result as differences
differences = female_penguin_species.difference(male_penguin_species)

# Print the differences
print(differences)