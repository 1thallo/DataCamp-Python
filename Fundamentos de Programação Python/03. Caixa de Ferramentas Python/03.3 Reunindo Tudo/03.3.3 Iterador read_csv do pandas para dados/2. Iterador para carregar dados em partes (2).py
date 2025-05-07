"""
Escrevendo um iterador para carregar dados em partes (2)

No exercício anterior, você usou read_csv() para ler partes de DataFrame de um grande conjunto de dados. 
Neste exercício, você lerá um arquivo usando um tamanho de bloco de DataFrame maior e, em seguida, processará os dados do primeiro bloco.

Para processar os dados, você criará outro DataFrame composto apenas pelas linhas de um país específico. 
Em seguida, você unirá duas das colunas do novo DataFrame, 'Total Population' e 'Urban population (% of total)'. 
Por fim, você criará uma lista de tuplas a partir do objeto zip, em que cada tupla é composta pelo valor de cada uma das duas colunas mencionadas.

Você usará os dados de 'ind_pop_data.csv', disponíveis em seu diretório atual. pandas foi importado como pd.

Instruções:
1. Use pd.read_csv() para ler o arquivo 'ind_pop_data.csv' em blocos de tamanho 1000. Atribua o resultado a urb_pop_reader.
2. Obtenha o primeiro bloco de DataFrame do iterável urb_pop_reader e atribua-o a df_urb_pop.
3. Selecione apenas as linhas de df_urb_pop que tenham um 'CountryCode' de 'CEB'. 
   Para fazer isso, compare se df_urb_pop['CountryCode'] é igual a 'CEB' dentro dos colchetes em df_urb_pop[____].
4. Usando zip(), junte as colunas 'Total Population' e 'Urban population (% of total)' de df_pop_ceb. 
   Atribua o objeto zip resultante a pops.
"""

# --- Código abaixo ---

# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)

# Get the first DataFrame chunk: df_urb_pop
df_urb_pop = next(urb_pop_reader)

# Check out the head of the DataFrame
print(df_urb_pop.head())

# Check out specific country: df_pop_ceb
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

# Zip DataFrame columns of interest: pops
pops = zip(df_pop_ceb['Total Population'], df_pop_ceb['Urban population (% of total)'])

# Turn zip object into list: pops_list
pops_list = list(pops)

# Print pops_list
print(pops_list)