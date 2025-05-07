"""
Compactação de dicionários

Para este exercício, você usará o que aprendeu sobre a função zip() e combinará duas listas em um dicionário.

Essas listas são, na verdade, extraídas de um arquivo de conjunto de dados maior de indicadores de desenvolvimento mundial do Banco Mundial. 
Para fins pedagógicos, pré-processamos esse conjunto de dados nas listas com as quais você trabalhará.

A primeira lista feature_names contém nomes de cabeçalho do conjunto de dados e a segunda lista row_vals contém valores reais de uma linha do conjunto de dados, correspondentes a cada um dos nomes de cabeçalho.

Instruções:
1. Crie um objeto zip chamando zip() e passando para ele feature_names e row_vals. Atribua o resultado a zipped_lists.
2. Crie um dicionário a partir do objeto zip zipped_lists chamando dict() com zipped_lists. Atribua o dicionário resultante a rs_dict.
"""

# --- Código abaixo ---

# Zip lists: zipped_lists
zipped_lists = zip(feature_names, row_vals)

# Create a dictionary: rs_dict
rs_dict = dict(zipped_lists)

# Print the dictionary
print(rs_dict)