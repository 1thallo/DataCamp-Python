# Iteração sobre Iteráveis

# Enunciado:
# Ótimo, você já sabe o que são iteráveis e iteradores!
# Neste exercício, você reforçará seu conhecimento sobre eles ao iterar e imprimir a partir de iteráveis e iteradores.
#
# Você recebe uma lista de strings `flash`. Você praticará a iteração sobre a lista usando um loop for.
# Você também criará um iterador para a lista e acessará os valores do iterador.

# ## Instruções:
# 1. Crie um loop for para percorrer `flash` e imprimir os valores na lista. Use `person` como a variável do loop.
# 2. Crie um iterador para a lista `flash` e atribua o resultado a `superhero`.
# 3. Imprima cada um dos itens de `superhero` usando `next()` 4 vezes.

# --- Código abaixo ---

# 1. Criar uma lista de strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# 2. Imprimir cada item da lista flash usando um loop for
for person in flash:
    print(person)

# 3. Criar um iterador para flash: superhero
superhero = iter(flash)

# 4. Imprimir cada item do iterador usando next()
print(next(superhero))
print(next(superhero))
print(next(superhero))
print(next(superhero))