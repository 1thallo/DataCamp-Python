# Anexar a uma Lista

# Enunciado:
# Você recebeu um dicionário chamado `authors`, que contém informações sobre 20 dos autores de ficção mais populares do mundo.
# Ele contém os nomes dos autores como chaves e o número de livros que eles criaram como valores.
#
# Você está interessado em descobrir quantos desses autores produziram menos de 25 livros.
# Para fazer isso, você criará uma lista chamada `authors_below_twenty_five`, preenchendo-a com nomes de autores
# condicionalmente com base no fato de eles terem criado menos de 25 livros.

# ## Instruções:
# 1. Crie uma lista vazia chamada `authors_below_twenty_five`.
# 2. Percorra os iteradores `key` e `value` no dicionário `authors`.
# 3. Dentro do loop for, verifique se o iterador `value` é menor que 25.
# 4. Se for o caso, acrescente o nome do autor à lista `authors_below_twenty_five`.

# --- Código abaixo ---

# 1. Criação de uma lista vazia para armazenar autores com menos de 25 livros
authors_below_twenty_five = []

# 2. Loop através do dicionário authors
for key, value in authors.items():
    if value < 25:
        authors_below_twenty_five.append(key)

print(authors_below_twenty_five)