# Trabalhando com Pandas

# Enunciado:
# pandas é um exemplo de um pacote Python popular.
#
# Neste exercício, o dicionário `sales` foi criado e disponibilizado para você, e sua tarefa é convertê-lo
# em um DataFrame do pandas e visualizar as cinco primeiras linhas.

# ## Instruções:
# 1. Importe o módulo `pandas` usando um alias de `pd`.
# 2. Crie `sales_df` usando uma função pandas para converter `sales` em um DataFrame.
# 3. Visualize as cinco primeiras linhas de `sales_df`.

# --- Código abaixo ---

# 1. Importar pandas como pd
import pandas as pd

# 2. Converter sales para um DataFrame do pandas
sales_df = pd.DataFrame(sales)

# 3. Visualizar as cinco primeiras linhas
print(sales_df.head())