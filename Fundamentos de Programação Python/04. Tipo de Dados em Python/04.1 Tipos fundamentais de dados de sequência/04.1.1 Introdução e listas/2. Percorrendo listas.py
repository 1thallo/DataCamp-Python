"""
Percorrendo listas

Anteriormente, você usou um loop for para iterar sobre uma lista, mas também pode usar uma compreensão de lista. 
As compreensões de lista assumem a forma de [action for item in list] e retornam uma nova lista.

Podemos usar a função sorted() para classificar os dados em uma lista do menor para o maior no caso de números 
e em ordem alfabética se a lista contiver cadeias de caracteres. 
A função sorted() retorna uma nova lista e não afeta a lista que você passou para a função.

Uma lista de listas, records, foi pré-carregada, e cada entrada é uma lista neste formato:
['2014','F','20799','Emma']
"""

# --- Código abaixo ---

# Create the list comprehension: baby_names
baby_names = [row[3] for row in records]
    
# Print the sorted baby names in ascending alphabetical order
print(sorted(baby_names))