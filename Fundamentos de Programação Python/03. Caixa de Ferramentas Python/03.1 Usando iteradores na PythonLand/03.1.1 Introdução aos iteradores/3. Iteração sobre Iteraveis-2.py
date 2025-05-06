# Iteração sobre Iteráveis (2)

# Enunciado:
# Uma das coisas que você aprendeu neste capítulo é que nem todos os iteráveis são listas reais.
# Alguns exemplos que examinamos são as strings e o uso da função `range()`.
#
# Você pode usar `range()` em um loop for como se fosse uma lista a ser iterada:
#
# for i in range(5):
#     print(i)
#
# Lembre-se de que `range()` não cria de fato a lista; em vez disso, ela cria um objeto range com um iterador
# que produz os valores até atingir o limite. Se `range()` criasse a lista real, chamá-la com um valor muito grande
# poderia ultrapassar a memória de um computador comum.
#
# Sua tarefa neste exercício é mostrar que ao chamar `range()` com um valor muito grande, ele não criará previamente a lista.

# ## Instruções:
# 1. Crie um objeto iterador `small_value` em `range(3)` usando a função `iter()`.
# 2. Usando um loop for, itere sobre `range(3)`, imprimindo o valor para cada iteração. Use `num` como a variável do loop.
# 3. Crie um objeto iterador `googol` em `range(10 ** 100)`.

# --- Código abaixo ---

# 1. Criar um iterador para range(3): small_value
small_value = iter(range(3))

# Imprimir os valores em small_value
print(next(small_value))
print(next(small_value))
print(next(small_value))

# 2. Iterar sobre range(3) e imprimir os valores
for num in range(3):
    print(num)

# 3. Criar um iterador para range(10 ** 100): googol
googol = iter(range(10 ** 100))

# Imprimir os primeiros 5 valores de googol
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))