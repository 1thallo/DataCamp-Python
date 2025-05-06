"""
Compreensões de listas condicionais para dados com registro de data e hora

Ótimo, você conseguiu extrair os dados de interesse, a hora, de um DataFrame do pandas! 
Vamos aprimorar ainda mais o seu trabalho adicionando uma condicional que especifique quais entradas devem ser selecionadas.

Neste exercício, você usará uma compreensão de lista para extrair a hora de dados do Twitter com registro de data e hora. 
Você adicionará uma expressão condicional à compreensão da lista para selecionar apenas as vezes em que entry[17:19] é igual a '19'. 
O pacote pandas foi importado como pd e o arquivo 'tweets.csv' foi importado como um DataFrame df para você usar.

Instruções:
1. Extraia a coluna 'created_at' de df e atribua o resultado a tweet_time.
2. Crie uma compreensão de lista que extraia a hora de cada linha em tweet_time. 
   Cada linha é uma string que representa um carimbo de data/hora, e você acessará os caracteres 12 a 19 da string para extrair a hora. 
   Use entry como a variável do iterador e atribua o resultado a tweet_clock_time. 
   Além disso, adicione uma expressão condicional que verifique se entry[17:19] é igual a '19'.
"""

# --- Código abaixo ---

# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']

# Print the extracted times
print(tweet_clock_time)