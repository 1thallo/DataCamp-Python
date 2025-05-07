"""
Transformando tudo isso em um DataFrame

Você juntou listas, criou uma função para conter o seu código e até usou a função em uma compreensão de lista para gerar uma lista de dicionários. 
Deu trabalho, mas você se saiu muito bem!

Agora você usará tudo isso para converter a lista de dicionários em um DataFrame do pandas. 
Você verá como é conveniente gerar um DataFrame a partir de dicionários com a função DataFrame() do pacote pandas.

A função lists2dict(), a lista feature_names e a lista row_lists foram pré-carregadas para este exercício.

Instruções:
1. Para usar a função DataFrame() que você precisa, primeiro importe o pacote pandas com o alias pd.
2. Crie um DataFrame a partir da lista de dicionários em list_of_dicts, chamando pd.DataFrame(). Atribua o DataFrame resultante a df.
3. Inspecione o conteúdo de df imprimindo o cabeçalho do DataFrame. O cabeçalho do DataFrame df pode ser acessado chamando df.head().
"""

# --- Código abaixo ---

# Import the pandas package
import pandas as pd

# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

# Turn list of dicts into a DataFrame: df
df = pd.DataFrame(list_of_dicts)

# Print the head of the DataFrame
print(df.head())