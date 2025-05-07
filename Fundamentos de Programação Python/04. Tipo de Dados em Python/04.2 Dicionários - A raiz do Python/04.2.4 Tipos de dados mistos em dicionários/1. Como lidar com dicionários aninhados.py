"""
Como lidar com dicionários aninhados

Um dicionário pode conter outro dicionário como o valor de uma chave, e essa é uma maneira muito comum de lidar com estruturas de dados repetitivas, 
como dados anuais, mensais ou semanais. Todas as mesmas regras se aplicam ao criar ou acessar o dicionário.

Por exemplo, se você tivesse um dicionário com uma classificação do meu consumo de cookies por ano e tipo de cookie. 
Ela deve ficar assim cookies = {'2017': {'chocolate chip': 483, 'peanut butter': 115}, 
'2016': {'chocolate chip': 9513, 'peanut butter': 6792}}. 
Eu poderia acessar quantos biscoitos de chocolate eu comi em 2016 usando cookies['2016']['chocolate chip'].

Ao explorar um novo dicionário, pode ser útil usar o método .keys() para ter uma ideia de quais dados podem estar disponíveis no dicionário. 
Você também pode iterar sobre um dicionário e ele retornará cada chave do dicionário para usar dentro do loop.

Carregamos um dicionário squirrels_by_park com nomes de parques para as chaves e um dicionário aninhado de dados de esquilos.
"""

# --- Código abaixo ---

# Print a list of keys from the squirrels_by_park dictionary
print(squirrels_by_park.keys())

# Print the keys from the squirrels_by_park dictionary for 'Union Square Park'
print(squirrels_by_park['Union Square Park'].keys())

# Loop over the dictionary
for park_name in squirrels_by_park:
    # Safely print the park_name and the highlights_in_fur_color or 'N/A'
    print(park_name, squirrels_by_park[park_name].get('highlights_in_fur_color', 'N/A'))