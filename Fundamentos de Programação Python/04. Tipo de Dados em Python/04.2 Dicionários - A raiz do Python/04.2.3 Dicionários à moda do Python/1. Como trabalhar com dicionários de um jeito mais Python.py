"""
Como trabalhar com dicionários de um jeito mais Python

Até agora, você trabalhou muito com as chaves de um dicionário para acessar dados, mas em Python, a maneira preferida de iterar sobre os itens em um dicionário é com o método .items().

Isso retorna cada chave e valor do dicionário como uma tupla, que você pode descompactar em um loop for. Agora você vai praticar fazer isso.

Carregamos um dicionário squirrels_by_park, e a chave Madison Square Park contém uma lista de dicionários.
"""

# --- Código abaixo ---

# Iterate over the first squirrel entry in the Madison Square Park list
for field, value in squirrels_by_park["Madison Square Park"][0].items():
    # Print field and value
    print(field, value)

print('-' * 13)

# Iterate over the second squirrel entry in the Madison Square Park list
for field, value in squirrels_by_park["Union Square Park"][1].items():
    # Print field and value
    print(field, value)