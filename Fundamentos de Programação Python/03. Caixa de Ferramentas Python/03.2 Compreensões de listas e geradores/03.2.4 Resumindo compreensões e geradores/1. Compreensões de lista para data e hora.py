"""
Compreensões de lista para data e hora

Agora você usará o que aprendeu neste capítulo para resolver um problema simples de extração de dados. 
Você também será apresentado a uma estrutura de dados, a pandas Series, neste exercício. 
Não vamos falar muito sobre isso aqui, mas o que você deve saber é que se trata de uma estrutura de dados com a qual você trabalhará muitas vezes ao analisar dados de DataFrames do pandas. 
Você pode pensar nas colunas do DataFrame como matrizes de dimensão única chamadas Series.

Neste exercício, você usará uma compreensão de lista para extrair a hora de dados do Twitter com registro de data e hora. 
O pacote pandas foi importado como pd e o arquivo 'tweets.csv' foi importado como um DataFrame df para você usar.

Instruções:
1. Extraia a coluna 'created_at' de df e atribua o resultado a tweet_time. 
   Fato interessante: a coluna extraída em tweet_time aqui é uma estrutura de dados Series!
2. Crie uma compreensão de lista que extraia a hora de cada linha em tweet_time. 
   Cada linha é uma string que representa um carimbo de data/hora, e você acessará os caracteres 12 a 19 da string para extrair a hora. 
   Use entry como a variável do iterador e atribua o resultado a tweet_clock_time. 
   Lembre-se de que o Python usa indexação baseada em 0.
"""

# --- Código abaixo ---

# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time]

# Print the extracted times
print(tweet_clock_time)