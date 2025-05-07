"""
Como lidar com tipos mistos aninhados

Anteriormente, usamos a expressão in para ver se os dados estão em um dicionário, como if 'cookies' in recipes_dict. 
Mas, e se quisermos encontrar dados em uma chave de dicionário que é uma lista de dicionários? 
Nesse cenário, podemos usar um loop for para percorrer os itens da lista aninhada e operar sobre eles. 
Além disso, podemos aproveitar as compreensões de lista para filtrar listas aninhadas de dicionários. 
Por exemplo: [cookie for cookie in recipes["cookies"] if "chocolate chip" in cookie["name"]] retornaria uma lista de cookies 
na lista de receitas que têm «chocolate chip» na chave de nome do cookie.

Carregamos um dicionário squirrels_by_park com nomes de parques para as chaves e uma lista de dicionários dos esquilos.
"""

# --- Código abaixo ---

# Use a for loop to iterate over the squirrels in Tompkins Square Park:
for squirrel in squirrels_by_park["Tompkins Square Park"]:
    # Safely print the activities of each squirrel or None
    print(squirrel.get("activities"))
    
# Print the list of 'Cinnamon' primary_fur_color squirrels in Union Square Park
print([squirrel for squirrel in squirrels_by_park["Union Square Park"] if squirrel["primary_fur_color"] == "Cinnamon"])