"""
Como criar tuplas nomeadas para armazenar dados

Muitas vezes, ao trabalhar com dados, você usará um dicionário apenas para poder usar nomes de chaves para facilitar a leitura do código e o acesso aos dados. 
O Python tem outro contêiner chamado namedtuple que é uma tupla, mas tem nomes para cada posição da tupla. 
Você cria uma passando um nome para o tipo da tupla e uma lista de nomes de campos.

Por exemplo, Cookie = namedtuple("Cookie", ['name', 'quantity']) criará um contêiner, e você pode criar outros desse tipo usando Cookie('chocolate chip', 1) 
onde você pode acessar o nome usando o atributo name e, em seguida, obter a quantidade usando o atributo quantity.

Neste exercício, você vai reestruturar os dados de registro de peso dos pinguins com os quais tem trabalhado em tuplas nomeadas para obter um código mais descritivo.

Instruções
100 XP
- Importe namedtuple de collections.
- Crie uma tupla nomeada chamada SpeciesDetails com um nome de tipo SpeciesDetails e os campos 'species', 'sex' e 'body_mass'.
- Crie uma lista chamada labeled_entries.
- Itere sobre a lista weight_log, desempacotando-a em species, sex e body_mass, 
  e crie uma nova instância de tupla nomeada SpeciesDetails para cada entrada e anexe-a à lista labeled_entries.
"""

# -- Código --

# Import namedtuple from collections
from collections import namedtuple

# Create the namedtuple: SpeciesDetails
SpeciesDetails = namedtuple('SpeciesDetails', ['species', 'sex', 'body_mass'])

# Create the empty list: labeled_entries
labeled_entries = []

# Iterate over the weight_log entries
for species, sex, body_mass in weight_log:
    # Append a new SpeciesDetails namedtuple instance for each entry to labeled_entries
    labeled_entries.append(SpeciesDetails(species, sex, body_mass))
    
print(labeled_entries[:5])
