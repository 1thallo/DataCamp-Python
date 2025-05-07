"""
Adição e ampliação de dicionários

Se você tiver um dicionário e quiser acrescentar dados a ele, basta criar uma nova chave e atribuir os dados desejados a ela. 
É importante lembrar que, se for um dicionário aninhado, todas as chaves no caminho de dados devem existir e cada chave no caminho deve ser atribuída individualmente.

Você também pode usar o método .update() para atualizar um dicionário com uma lista de chaves e valores de outro dicionário, tuplas ou argumentos de palavras-chave.

O dicionário squirrels_by_park já está carregado para você, que tem como chave o nome do parque e o valor é uma tupla com a cor principal, 
os destaques, a ação e a reação aos humanos.
"""

# --- Código abaixo ---

# Assign squirrels_madison as the value to the 'Madison Square Park' key
squirrels_by_park['Madison Square Park'] = squirrels_madison

# Update squirrels_by_park with the squirrels_union tuple
squirrels_by_park.update([squirrels_union])

# Loop over the park_name in the squirrels_by_park dictionary 
for park_name in squirrels_by_park:
    # Safely print a list of the primary_fur_color for each squirrel in park_name
    print(park_name, [squirrel.get('primary_fur_color', 'N/A') for squirrel in squirrels_by_park[park_name]]) 