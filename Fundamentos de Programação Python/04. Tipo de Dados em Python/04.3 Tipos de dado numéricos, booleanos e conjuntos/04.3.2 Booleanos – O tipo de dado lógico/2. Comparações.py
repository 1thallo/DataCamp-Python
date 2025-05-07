"""
Comparações

Os booleanos e sua veracidade são usados com mais frequência em comparações, e usamos comparações sem sequer pensar no tipo de dado subjacente. 
Para realizar uma comparação, podemos usar um operador de comparação. O Python oferece suporte aos seguintes operadores de comparação:

== igual a
!= diferente de
> maior que
< menor que
>= maior ou igual
<= menor ou igual 

Para este exercício, usaremos um subconjunto do conjunto de dados de pinguins do Arquipélago de Palmer (Antártica), denominado penguins, 
como uma lista de dicionários com as chaves de species, flipper_length, body_mass e sex.
"""

# --- Código abaixo ---

# Use a for loop to iterate over the penguins list
for penguin in penguins:
    # Check the penguin entry for a body mass of more than 3300 grams
    if penguin["body_mass"] > 3300:
        # Print the species and sex of the penguin if true
        print(f"{penguin['species']} - {penguin['sex']}")