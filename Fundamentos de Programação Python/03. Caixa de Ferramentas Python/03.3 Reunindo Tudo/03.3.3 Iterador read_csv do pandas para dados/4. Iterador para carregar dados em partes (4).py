"""
Escrevendo um iterador para carregar dados em partes (4)

Nos exercícios anteriores, você processou apenas os dados do primeiro bloco do DataFrame. 
Desta vez, você agregará os resultados a todos os blocos do DataFrame no conjunto de dados. 
Isso significa basicamente que você vai processar todo o conjunto de dados agora. 
Isso é bem legal porque você poderá processar todo o grande conjunto de dados trabalhando apenas em partes menores dele!

Você usará os dados de 'ind_pop_data.csv', disponíveis em seu diretório atual. 
Os pacotes pandas e matplotlib.pyplot foram importados como pd e plt, respectivamente, para você usar.

Instruções:
1. Inicialize um DataFrame vazio data usando pd.DataFrame().
2. No loop for, itere sobre urb_pop_reader para que você possa processar todos os blocos de DataFrame no conjunto de dados.
3. Concatene data e df_pop_ceb passando uma lista de DataFrames para pd.concat().
"""

# --- Código abaixo ---

# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)

# Initialize empty DataFrame: data
data = pd.DataFrame()

# Iterate over each DataFrame chunk
for df_urb_pop in urb_pop_reader:

    # Check out specific country: df_pop_ceb
    df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

    # Zip DataFrame columns of interest: pops
    pops = zip(df_pop_ceb['Total Population'],
               df_pop_ceb['Urban population (% of total)'])

    # Turn zip object into list: pops_list
    pops_list = list(pops)

    # Use list comprehension to create new DataFrame column 'Total Urban Population'
    df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]
    
    # Concatenate DataFrame chunk to the end of data: data
    data = pd.concat([data, df_pop_ceb])

# Plot urban population data
data.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()