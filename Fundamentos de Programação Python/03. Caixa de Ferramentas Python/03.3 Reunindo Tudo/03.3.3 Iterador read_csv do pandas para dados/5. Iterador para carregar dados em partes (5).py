"""
Escrevendo um iterador para carregar dados em partes (5)

Essa é a última etapa. Você aprendeu muito sobre o processamento de um grande conjunto de dados em partes. 
Neste último exercício, você colocará todo o código para processar os dados em uma única função, de modo que possa reutilizar o código sem precisar escrever tudo de novo.

Você definirá a função plot_pop() que recebe dois argumentos: o nome do arquivo a ser processado e o código do país das linhas que você deseja processar no conjunto de dados.

Como todo o código anterior que você escreveu nos exercícios anteriores estará contido na função plot_pop(), chamar a função já faz o seguinte:
- Carregamento do arquivo, parte por parte,
- Criação da nova coluna de valores da população urbana e
- Plotagem dos dados da população urbana.

Você usará os dados de 'ind_pop_data.csv', disponíveis em seu diretório atual. 
Os pacotes pandas e matplotlib.pyplot foram importados como pd e plt, respectivamente, para você usar.

Instruções:
1. Defina a função plot_pop() que tem dois argumentos: o primeiro é filename para o arquivo a ser processado e o segundo é country_code para o país a ser processado no conjunto de dados.
2. Chame plot_pop() para processar os dados do código de país 'CEB' no arquivo 'ind_pop_data.csv'.
3. Chame plot_pop() para processar os dados do código de país 'ARB' no arquivo 'ind_pop_data.csv'.
"""

# --- Código abaixo ---

# Define plot_pop()
def plot_pop(filename, country_code):
    """Processa dados de população urbana e cria um gráfico de dispersão."""

    # Initialize reader object: urb_pop_reader
    urb_pop_reader = pd.read_csv(filename, chunksize=1000)

    # Initialize empty DataFrame: data
    data = pd.DataFrame()
    
    # Iterate over each DataFrame chunk
    for df_urb_pop in urb_pop_reader:
        # Check out specific country: df_pop_ceb
        df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == country_code]

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

# Set the filename: fn
fn = 'ind_pop_data.csv'

# Call plot_pop for country code 'CEB'
plot_pop(fn, 'CEB')

# Call plot_pop for country code 'ARB'
plot_pop(fn, 'ARB')