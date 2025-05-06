# Realização de Cálculos com pandas

# Enunciado:
# Agora, você recebeu um arquivo CSV chamado `sales.csv` que contém dados de vendas com três colunas:
# "user_id", "date", e "order_value".
#
# Usando o pandas, você lerá o arquivo e calculará as estatísticas sobre os valores de vendas.
#
# Da mesma forma que você pode acessar um dicionário pela sua chave, por exemplo, `dictionary["key_name"]`,
# você pode usar a mesma sintaxe em pandas para acessar uma coluna!
# Além disso, o pacote também oferece métodos úteis para realizar cálculos em DataFrames ou subconjuntos de DataFrames (como colunas)!
#
# Exemplos dessa sintaxe incluem `df["column_name"].mean()` e `df["column_name"].sum()` para calcular a média
# e o total de uma determinada coluna, respectivamente.

# ## Instruções:
# 1. Leia "sales.csv", salvando como um DataFrame do pandas chamado `sales_df`.
# 2. Acesse a coluna "order_value" de `sales_df` e, em seguida, chame o método `.mean()` para encontrar o valor médio do pedido.
# 3. Acesse a coluna "order_value" de `sales_df` e, em seguida, chame o método `.sum()` para encontrar o valor total de todos os pedidos.

# --- Código abaixo ---

# 1. Ler o arquivo sales.csv
sales_df = pd.read_csv("sales.csv")

# 2. Calcular e imprimir o valor médio dos pedidos
print(sales_df["order_value"].mean())

# 3. Calcular e imprimir o valor total das vendas
print(sales_df["order_value"].sum())