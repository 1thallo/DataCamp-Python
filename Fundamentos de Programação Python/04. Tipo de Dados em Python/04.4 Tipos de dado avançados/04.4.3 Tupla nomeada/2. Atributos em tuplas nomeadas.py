"""
Como usar atributos em tuplas nomeadas

Quando você tiver uma tupla nomeada, poderá escrever um código mais expressivo e fácil de entender. 
Lembre-se, você pode acessar os elementos na tupla pelo nome deles como um atributo. 
Por exemplo, você pode acessar as species das tuplas nomeadas do exercício anterior usando o atributo .species.

Aqui, você usará as tuplas que criou no exercício anterior para ver como isso funciona.

Instruções
100 XP
Itere entre as primeiras vinte entrys na lista labeled_entries:
Se for uma espécie Chinstrap:
Imprima sex e body_mass das entrys separados por :.
"""

# -- Código --

# Iterate over the first twenty entries in labeled_entries
for entry in labeled_entries[0:20]:
    # if the entry's species equals Chinstrap
    if entry.species == 'Chinstrap':
        # Print each entry's sex and body_mass separated by a colon
        print(f'{entry.sex}:{entry.body_mass}')
