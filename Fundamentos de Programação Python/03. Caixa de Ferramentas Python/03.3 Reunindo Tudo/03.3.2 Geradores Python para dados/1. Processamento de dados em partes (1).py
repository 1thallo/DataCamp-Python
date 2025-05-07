"""
Processamento de dados em partes (1)

Às vezes, as fontes de dados podem ser tão grandes que o armazenamento de todo o conjunto de dados na memória consome recursos demais. 
Neste exercício, você processará as primeiras 1.000 linhas de um arquivo, linha por linha, para criar um dicionário de quantas vezes cada país aparece em uma coluna do conjunto de dados.

Use o arquivo csv 'world_dev_ind.csv' que está no diretório atual. 
Para começar, você precisa abrir uma conexão com esse arquivo usando o que é conhecido como gerenciador de contexto. 
Por exemplo, o comando with open('datacamp.csv') as datacamp vincula o arquivo csv 'datacamp.csv' como datacamp no gerenciador de contexto. 
Aqui, a instrução with é o gerenciador de contexto e sua finalidade é garantir que os recursos sejam alocados de forma eficiente ao abrir uma conexão com um arquivo.

Instruções:
1. Use open() para associar o arquivo csv 'world_dev_ind.csv' como file no gerenciador de contexto.
2. Complete o loop for de modo que ele itere 1.000 vezes para executar o corpo do loop e processar somente as primeiras 1.000 linhas de dados do arquivo.
"""

# --- Código abaixo ---

# Open a connection to the file
with open('world_dev_ind.csv') as file:

    # Skip the column names
    file.readline()

    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Process only the first 1000 rows
    for j in range(0, 1000):

        # Split the current line into a list: line
        line = file.readline().split(',')

        # Get the value for the first column: first_col
        first_col = line[0]

        # If the column value is in the dict, increment its value
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1

        # Else, add to the dict and set value to 1
        else:
            counts_dict[first_col] = 1

# Print the resulting dictionary
print(counts_dict)