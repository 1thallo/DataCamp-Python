"""
Iterador para carregar dados em partes (3)

Você já está se acostumando a ler e processar dados em blocos. Vamos aprimorar um pouco mais suas habilidades adicionando uma coluna a um DataFrame.

A partir do código do exercício anterior, você usará uma compreensão de lista para criar os valores de uma nova coluna 'Total Urban Population' 
a partir da lista de tuplas que você gerou anteriormente. Lembre-se de que, no exercício anterior, o primeiro e o segundo elementos de cada tupla consistem, 
respectivamente, nos valores das colunas 'Total Population' e 'Urban population (% of total)'. 
Os valores nessa nova coluna 'Total Urban Population', portanto, são o produto do primeiro e do segundo elemento em cada tupla. 
Além disso, como o segundo elemento é uma porcentagem, você precisa dividir o resultado inteiro por 100 ou, alternativamente, multiplicá-lo por 0.01.

Você também plotará os dados dessa nova coluna para criar uma visualização dos dados da população urbana.

Os pacotes pandas e matplotlib.pyplot foram importados como pd e plt, respectivamente, para você usar.

Instruções:
1. Escreva uma compreensão de lista para gerar uma lista de valores de pops_list para a nova coluna 'Total Urban Population'. 
   A expressão de saída deve ser o produto do primeiro e do segundo elemento de cada tupla em pops_list. 
   Como o segundo elemento é uma porcentagem, você também precisa multiplicar o resultado por 0.01 ou dividi-lo por 100. 
   Além disso, observe que a coluna 'Total Urban Population' só deve ser capaz de receber valores inteiros. 
   Para garantir isso, certifique-se de converter a expressão de saída em um número inteiro com int().
2. Crie um gráfico de dispersão em que o eixo x são os valores da coluna 'Year' e o eixo y são os valores da coluna 'Total Urban Population'.
"""

# --- Código abaixo ---

# Code from previous exercise
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)
df_urb_pop = next(urb_pop_reader)
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']
pops = zip(df_pop_ceb['Total Population'], 
           df_pop_ceb['Urban population (% of total)'])
pops_list = list(pops)

# Use list comprehension to create new DataFrame column 'Total Urban Population'
df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]

# Plot urban population data
df_pop_ceb.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()