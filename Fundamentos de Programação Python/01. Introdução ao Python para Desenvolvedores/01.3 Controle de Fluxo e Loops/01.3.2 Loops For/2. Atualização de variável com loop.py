# Atualização de uma Variável com Loops For

# Enunciado:
# Você está planejando dar uma festa para mostrar sua playlist aos amigos e familiares.
# Você alugou um local com capacidade máxima de 30 pessoas e gostaria de controlar os ingressos vendidos.
# Essa é a oportunidade perfeita para você usar um loop for: ele incrementará o valor de uma variável
# cada vez que um ingresso for vendido e, em seguida, imprimirá uma declaração quando o evento estiver esgotado.

# ## Instruções:
# 1. Crie uma variável chamada `tickets_sold` com um valor de 0.
# 2. Crie uma variável chamada `max_capacity` com um valor de 30.
# 3. Percorra um intervalo começando em 1 e terminando em `max_capacity` mais um, nomeando o iterador como `tickets`.
# 4. Dentro do loop for, adicione 1 ao valor de `tickets_sold`.

# --- Código abaixo ---

# Criação da variável tickets_sold com valor inicial 0
tickets_sold = 0

# Criação da variável max_capacity com valor máximo de 30
max_capacity = 30

# Loop através de um intervalo de 1 até max_capacity (inclusive)
for i in range(1, max_capacity + 1):
    # Incrementa tickets_sold em 1 a cada iteração
    tickets_sold += 1

# Exibição da mensagem indicando que os ingressos estão esgotados
print("Sold out:", tickets_sold, "tickets sold!")