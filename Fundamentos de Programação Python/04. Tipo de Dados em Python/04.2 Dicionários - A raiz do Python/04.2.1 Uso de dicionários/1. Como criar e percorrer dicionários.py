"""
Como criar e percorrer dicionários

Com frequência, você vai se deparar com a necessidade de fazer um loop sobre alguns dados do tipo matriz, como no Capítulo 1, 
e fornecer a eles alguma estrutura para encontrar rapidamente os dados que deseja.

Você começa criando um dicionário vazio e atribuindo parte dos dados da matriz como a chave e o restante como o valor.

Anteriormente, você usou sorted() para organizar seus dados em uma lista. Os dicionários também podem ser ordenados. 
Por padrão, ao usar sorted() em um dicionário, você classificará pelas chaves do dicionário.

O objetivo deste exercício é que você se familiarize com a criação de dicionários percorrendo alguma fonte de dados 
e, em seguida, percorrendo o dicionário para usar esses dados.
"""

# --- Código abaixo ---

# Create an empty dictionary: squirrels_by_park
squirrels_by_park = {}

# Loop over the squirrels list and unpack each tuple
for park, squirrel_details in squirrels:
    # Add each squirrel_details to the squirrels_by_park dictionary 
    squirrels_by_park[park] = squirrel_details
    
# Sort the squirrels_by_park dict alphabetically by park
for park in sorted(squirrels_by_park):
    # Print each park and its value in squirrels_by_park
    print(f'{park}: {squirrels_by_park[park]}')