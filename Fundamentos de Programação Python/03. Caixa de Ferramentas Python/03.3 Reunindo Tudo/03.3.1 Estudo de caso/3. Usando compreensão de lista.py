"""
Usando uma compreensão de lista

Desta vez, você usará a função lists2dict() que definiu no último exercício para transformar uma série de listas em uma lista de dicionários com a ajuda de uma compreensão de lista.

A função lists2dict() já foi pré-carregada, juntamente com algumas listas, feature_names e row_lists. 
feature_names contém os nomes de cabeçalho do conjunto de dados do Banco Mundial e row_lists é uma lista de listas, 
em que cada sub-lista é uma lista de valores reais de uma linha do conjunto de dados.

Seu objetivo é usar uma compreensão de lista para gerar uma lista de dicionários, 
em que as chaves são os nomes de cabeçalho e os valores são as entradas de linha.

Instruções:
1. Inspecione o conteúdo de row_lists imprimindo as duas primeiras listas em row_lists.
2. Crie uma compreensão de lista que gere um dicionário usando lists2dict() para cada sub-lista em row_lists. 
   As chaves são da lista feature_names e os valores são as entradas de linha em row_lists. 
   Use sublist como sua variável de iterador e atribua a lista resultante de dicionários a list_of_dicts.
3. Consulte os dois primeiros dicionários em list_of_dicts, imprimindo-os.
"""

# --- Código abaixo ---

# Print the first two lists in row_lists
print(row_lists[0])
print(row_lists[1])

# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

# Print the first two dictionaries in list_of_dicts
print(list_of_dicts[0])
print(list_of_dicts[1])