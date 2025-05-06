# Funções Lambda com Iteráveis

# Enunciado:
# Você usou as funções lambda para executar ações em um único valor; agora é hora de testar como trabalhar com iteráveis.
#
# Você recebeu uma lista chamada `sales_prices` que contém os preços de venda de vários itens.
# Seu objetivo é usar uma função lambda para adicionar o imposto (20%) a cada valor da lista.

# ## Instruções:
# 1. Crie `add_taxes`, que multiplica cada valor em `sales_prices` por 20%.
# 2. Imprima uma lista usando `add_taxes` para atualizar os valores em `sales_prices`.

# --- Código abaixo ---

# Lista de preços de venda
sales_prices = [29.99, 9.95, 14.50, 39.75, 60.00]

# 1. Criar add_taxes para adicionar 20% a cada item em sales_prices
add_taxes = map(lambda x: x * 1.2, sales_prices)

# 2. Usar add_taxes para retornar uma nova lista com os valores atualizados
print(list(add_taxes))