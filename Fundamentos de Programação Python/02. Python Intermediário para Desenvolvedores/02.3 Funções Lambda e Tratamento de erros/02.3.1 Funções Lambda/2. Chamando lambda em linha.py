# Chamando Lambda em Linha

# Enunciado:
# Lembre-se de que um dos principais benefícios da lambda é a capacidade de usar funções em linha.
#
# Neste exercício, você modificará a abordagem do exercício anterior para adicionar imposto à variável `sale_price`
# em linha sem armazenar uma função lambda como variável primeiro.

# ## Instruções:
# 1. Em uma única linha de código, crie uma função lambda que multiplique `sale_price` por 1.2 e retorne o resultado.

# --- Código abaixo ---

# Variável de exemplo
sale_price = 29.99

# 1. Chamar uma função lambda em linha para adicionar 20% ao sale_price
print((lambda x: x * 1.2)(sale_price))