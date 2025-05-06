# Adição de Imposto

# Enunciado:
# É hora de testar suas habilidades com a função lambda!
#
# Neste exercício, você usará uma função lambda para adicionar um imposto de 20% ao custo da variável `sale_price`.

# ## Instruções:
# 1. Defina a função lambda `add_tax` para multiplicar o argumento fornecido a ela, `x`, por 1.2.
# 2. Chame `add_tax()` na variável `sale_price`.

# --- Código abaixo ---

# Variável de exemplo
sale_price = 29.99

# 1. Definir a função lambda add_tax
add_tax = lambda x: x * 1.2

# 2. Chamar a função lambda na variável sale_price
print(add_tax(sale_price))
