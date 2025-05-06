# Função do Conversor de Estrutura de Dados

# Enunciado:
# Agora que você aprendeu sobre os tipos de argumentos em funções, colocará isso em prática criando uma função
# personalizada que converte dados em diferentes estruturas.

# ## Instruções:
# 1. Defina `convert_data_structure` com dois argumentos: `data` e `data_type`, sendo que o último tem um valor padrão de `"list"`.
# 2. Adicione uma condição para verificar se `data_type` é `"tuple"`.
# 3. Caso contrário, se `data_type` for `"set"`, converta `data` em um conjunto, salvando-o como uma variável de mesmo nome.
# 4. Chame a função na estrutura de dados fornecida, usando um par de valores de argumento de palavra-chave apropriado para convertê-la em um conjunto.

# --- Código abaixo ---

def convert_data_structure(data, data_type="list"):
    if data_type == "tuple":
        data = tuple(data)
    elif data_type == "set":
        data = set(data)
    else:
        data = list(data)
    return data

convert_data_structure({"a", 1, "b", 2, "c", 3}, data_type="set")