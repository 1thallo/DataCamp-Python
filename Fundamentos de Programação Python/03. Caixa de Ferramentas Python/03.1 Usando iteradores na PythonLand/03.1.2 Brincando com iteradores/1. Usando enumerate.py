# Usando enumerate

# Enunciado:
# Você está mesmo pegando o jeito de usar iteradores, ótimo trabalho!
#
# Você acabou de adquirir várias ideias novas sobre iteradores no último vídeo e uma delas é a função `enumerate()`.
# Lembre-se de que `enumerate()` retorna um objeto enumerate que produz uma sequência de tuplas, e cada uma das tuplas
# é um par de valores de índice.
#
# Neste exercício, você receberá uma lista de strings `mutants` e praticará o uso do `enumerate()` com ela,
# imprimindo uma lista de tuplas e desempacotando as tuplas usando um loop for.

# ## Instruções:
# 1. Crie uma lista de tuplas em `mutants` e atribua o resultado a `mutant_list`. Certifique-se de gerar as tuplas
#    usando `enumerate()` e transforme o resultado em uma lista usando `list()`.
# 2. Conclua o primeiro loop for desempacotando as tuplas geradas pela chamada de `enumerate()` em `mutants`.
#    Use `index1` para o índice e `value1` para o valor ao desempacotar a tupla.
# 3. Conclua o segundo loop for de modo semelhante ao primeiro, mas, desta vez, altere o índice inicial para começar
#    em 1, passando-o como argumento para o parâmetro `start` de `enumerate()`. Use `index2` para o índice e `value2`
#    para o valor ao desempacotar a tupla.

# --- Código abaixo ---

# 1. Criar uma lista de strings: mutants
mutants = ['charles xavier', 
           'bobby drake', 
           'kurt wagner', 
           'max eisenhardt', 
           'kitty pryde']

# 2. Criar uma lista de tuplas: mutant_list
mutant_list = list(enumerate(mutants))

# Imprimir a lista de tuplas
print(mutant_list)

# 3. Desempacotar e imprimir os pares de tuplas
for index1, value1 in enumerate(mutants):
    print(index1, value1)

# 4. Alterar o índice inicial para começar em 1
for index2, value2 in enumerate(mutants, start=1):
    print(index2, value2)