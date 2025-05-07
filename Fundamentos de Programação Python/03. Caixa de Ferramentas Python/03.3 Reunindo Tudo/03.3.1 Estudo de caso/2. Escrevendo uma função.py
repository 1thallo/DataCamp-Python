"""
Escrevendo uma função para ajudar você

Suponha que você precise repetir o mesmo processo feito no exercício anterior para muitas e muitas linhas de dados. 
Reescrever seu código várias vezes pode ser muito tedioso, repetitivo e impossível de dar manutenção.

Neste exercício, você criará uma função para abrigar o código que escreveu anteriormente para tornar as coisas mais fáceis e muito mais concisas. 
Por quê? Dessa forma, você só precisa chamar a função e fornecer as listas apropriadas para criar seus dicionários! 
Novamente, as listas feature_names e row_vals são pré-carregadas e contêm os nomes de cabeçalho do conjunto de dados e os valores reais de uma linha do conjunto de dados, respectivamente.

Instruções:
1. Defina a função lists2dict() com dois parâmetros: o primeiro é list1 e o segundo é list2.
2. Retorne o dicionário resultante rs_dict em lists2dict().
3. Chame a função lists2dict() com os argumentos feature_names e row_vals. Atribua o resultado da chamada da função a rs_fxn.
"""

# --- Código abaixo ---

# Define lists2dict()
def lists2dict(list1, list2):
    """Return a dictionary where list1 provides
    the keys and list2 provides the values."""

    # Zip lists: zipped_lists
    zipped_lists = zip(list1, list2)

    # Create a dictionary: rs_dict
    rs_dict = dict(zipped_lists)

    # Return the dictionary
    return rs_dict

# Call lists2dict: rs_fxn
rs_fxn = lists2dict(feature_names, row_vals)

# Print rs_fxn
print(rs_fxn)