"""
Escrevendo um gerador para carregar dados em partes (3)

Ótimo! Você acabou de criar uma função geradora que pode ser usada para ajudá-lo a processar arquivos grandes.

Agora, vamos usar sua função geradora para processar o conjunto de dados do Banco Mundial, como você fez anteriormente. 
Você processará o arquivo linha por linha para criar um dicionário de quantas vezes cada país aparece em uma coluna do conjunto de dados. 
No entanto, para este exercício, você não processará apenas 1.000 linhas de dados, mas sim todo o conjunto de dados!

A função geradora read_large_file() e o arquivo csv 'world_dev_ind.csv' estão pré-carregados e prontos para você usar.

Instruções:
1. Associe o arquivo 'world_dev_ind.csv' a file no gerenciador de contexto com open().
2. Complete o loop for de modo que ele itere sobre o gerador a partir da chamada de read_large_file() para processar todas as linhas do arquivo.
"""

# --- Código abaixo ---

# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Open a connection to the file
with open('world_dev_ind.csv') as file:

    # Iterate over the generator from read_large_file()
    for line in read_large_file(file):

        # Split the line into a list: row
        row = line.split(',')
        first_col = row[0]

        # Update the counts in the dictionary
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1

# Print the resulting dictionary
print(counts_dict)