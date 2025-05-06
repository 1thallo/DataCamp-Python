# Iteradores como Argumentos de Função

# Enunciado:
# Você está usando a função `iter()` para obter um objeto iterador, bem como a função `next()` para recuperar
# os valores do objeto iterador um a um.
#
# Há também funções que recebem iteradores e iteráveis como argumentos. Por exemplo, as funções `list()` e `sum()`
# retornam uma lista e a soma dos elementos, respectivamente.
#
# Neste exercício, você usará essas funções passando um iterável de `range()` e, em seguida, imprimindo os resultados
# das chamadas de função.

# ## Instruções:
# 1. Crie um objeto range que produza os valores de 10 a 20 usando `range()`. Atribua o resultado a `values`.
# 2. Use a função `list()` para criar uma lista de valores a partir do objeto de intervalo `values`. Atribua o resultado a `values_list`.
# 3. Use a função `sum()` para obter a soma dos valores de 10 a 20 do objeto de intervalo `values`. Atribua o resultado a `values_sum`.

# --- Código abaixo ---

# 1. Criar um objeto range que produza os valores de 10 a 20: values
values = range(10, 21)

# Imprimir o objeto range
print(values)

# 2. Criar uma lista de inteiros a partir do objeto range: values_list
values_list = list(values)

# Imprimir values_list
print(values_list)

# 3. Obter a soma dos valores de 10 a 20: values_sum
values_sum = sum(values)

# Imprimir values_sum
print(values_sum)