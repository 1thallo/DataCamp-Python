"""
Escrevendo um iterador para carregar dados em partes (1)

Outra maneira de ler dados grandes demais para serem armazenados na memória em partes é ler o arquivo como DataFrames de um determinado comprimento, por exemplo, 100. 
Por exemplo, com o pacote pandas (importado como pd), você pode fazer pd.read_csv(filename, chunksize=100). 
Isso cria um objeto leitor iterável, o que significa que você pode usar next() nele.

Neste exercício, você lerá um arquivo em pequenos partes de DataFrame com read_csv(). 
Você usará os dados do Indicadores do Banco Mundial 'ind_pop.csv', disponíveis em seu diretório atual, 
para examinar o indicador de população urbana de vários países e anos.

Instruções:
1. Use pd.read_csv() para ler blocos de tamanho 10 em 'ind_pop.csv'. Atribua o resultado a df_reader.
2. Imprima as duas primeiras partes de df_reader.
"""

# --- Código abaixo ---

# Import the pandas package
import pandas as pd

# Initialize reader object: df_reader
df_reader = pd.read_csv('ind_pop.csv', chunksize=10)

# Print two chunks
print(next(df_reader))
print(next(df_reader))