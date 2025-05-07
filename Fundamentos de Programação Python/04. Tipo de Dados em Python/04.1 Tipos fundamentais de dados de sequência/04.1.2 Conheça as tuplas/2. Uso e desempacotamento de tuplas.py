"""
Uso e desempacotamento de tuplas

Se você tiver uma tupla como ('chocolate chip cookies', 15) e quiser acessar cada parte dos dados, poderá usar um índice da mesma forma que em uma lista. 
No entanto, você também pode "desempacotar" a tupla em várias variáveis, como type, count = ('chocolate chip cookies', 15), 
que definirá type para 'chocolate chip cookies' e count para 15.

Muitas vezes, você desejará emparelhar vários tipos de dado de matriz. A função zip() faz exatamente isso. 
Ele retornará uma lista de tuplas contendo um elemento de cada lista passada para zip().

Ao percorrer uma lista, você também pode rastrear sua posição na lista usando a função enumerate(). 
A função retorna o índice do item da lista em que você está no momento e o próprio item da lista.
"""

# --- Código abaixo ---

# Pair up the girl and boy names: pairs
pairs = zip(girl_names, boy_names)

# Iterate over pairs
for rank, pair in enumerate(pairs):
    # Unpack pair: girl_name, boy_name
    girl_name, boy_name = pair
    # Print the rank and names associated with each rank
    print(f'Rank {rank+1}: {girl_name} and {boy_name}')