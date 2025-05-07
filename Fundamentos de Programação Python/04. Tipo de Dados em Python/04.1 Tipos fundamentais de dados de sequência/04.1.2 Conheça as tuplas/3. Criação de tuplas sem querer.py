"""
Criação de tuplas sem querer

As tuplas são muito úteis e poderosas, e é muito fácil criar uma sem querer. 
Tudo o que você precisa fazer é criar uma variável e adicionar uma vírgula depois da atribuição. 
Isso se torna um erro quando você tenta usar a variável mais tarde, esperando que ela seja uma string ou um número.

Você pode verificar o tipo de dado de uma variável com a função type(). 
Neste exercício, você verá como é fácil criar uma tupla sem querer.
"""

# --- Código abaixo ---

# Create the normal variable: normal
normal = 'simple'

# Create the mistaken variable: error
error = 'trailing comma',

# Print the types of the variables
print(type(normal))
print(type(error))