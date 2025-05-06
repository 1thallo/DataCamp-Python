"""
Extração de informações de grandes quantidades de dados do Twitter

Você fez um ótimo trabalho ao dividir esse arquivo no exercício anterior. 
Agora você sabe como lidar com situações em que precisa processar um arquivo muito grande, e essa é uma habilidade muito útil.

É bom saber como processar um arquivo em partes menores e mais gerenciáveis, mas pode se tornar muito entediante 
ter que escrever e reescrever o mesmo código para a mesma tarefa todas as vezes. 
Neste exercício, você tornará seu código mais reutilizável, colocando o trabalho do último exercício em uma definição de função.

O pacote pandas foi importado como pd e o arquivo 'tweets.csv' está no diretório atual para você usar.

Instruções:
1. Defina a função count_entries(), que tem 3 parâmetros. 
   O primeiro parâmetro é csv_file para o nome do arquivo, o segundo é c_size para o tamanho do bloco e o último é colname para o nome da coluna.
2. Itere sobre o arquivo em csv_file usando um loop for. 
   Use a variável de loop chunk e itere sobre a chamada de pd.read_csv(), passando c_size para chunksize.
3. No loop interno, itere sobre a coluna dada por colname em chunk usando um loop for. Use a variável de loop entry.
4. Chame a função count_entries() passando para ela o nome do arquivo 'tweets.csv', o tamanho dos blocos 10 e o nome da coluna a ser contada, 'lang'. 
   Atribua o resultado da chamada à variável result_counts.
"""

# --- Código abaixo ---

# Define count_entries()
def count_entries(csv_file, c_size, colname):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file, chunksize=c_size):

        # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1

    # Return counts_dict
    return counts_dict

# Call count_entries(): result_counts
result_counts = count_entries('tweets.csv', 10, 'lang')

# Print result_counts
print(result_counts)