"""
Processamento de grandes quantidades de dados

Às vezes, os dados que precisamos processar atingem um tamanho muito grande para a memória do computador. 
Esse é um problema comum enfrentado pelos cientistas de dados. 
Uma solução para isso é processar uma fonte de dados inteira, parte por parte, em vez de tudo de uma vez só.

Neste exercício, você fará exatamente isso. 
Você processará um grande arquivo csv de dados do Twitter da mesma forma que processou 'tweets.csv' em Reunindo tudo do curso de introdução, 
mas, desta vez, trabalhará nele em partes de 10 entradas por vez.

O pacote pandas foi importado como pd e o arquivo 'tweets.csv' está no diretório atual para você usar.

Esteja ciente de que esses são dados reais do Twitter e, portanto, há sempre o risco de que eles contenham palavrões ou outros conteúdos ofensivos.

Instruções:
1. Inicialize um dicionário vazio counts_dict para armazenar os resultados do processamento dos dados do Twitter.
2. Itere sobre o arquivo 'tweets.csv' usando um loop for. 
   Use a variável de loop chunk e itere sobre a chamada de pd.read_csv() com um chunksize de 10.
3. No loop interno, itere sobre a coluna 'lang' em chunk usando um loop for. Use a variável de loop entry.
"""

# --- Código abaixo ---

# Inicializar um dicionário vazio: counts_dict
counts_dict = {}

# Iterar sobre o arquivo em partes (chunks)
for chunk in pd.read_csv('tweets.csv', chunksize=10):

    # Iterar sobre a coluna 'lang' no DataFrame
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

# Imprimir o dicionário preenchido
print(counts_dict)