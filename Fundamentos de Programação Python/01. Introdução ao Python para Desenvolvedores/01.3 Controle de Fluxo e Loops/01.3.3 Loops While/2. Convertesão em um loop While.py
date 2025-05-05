# Convertesão em um Loop While

# Enunciado:
# Muitas vezes, você pode realizar as mesmas tarefas usando um loop for ou while.
# Para demonstrar isso, você converterá esse loop for em um while!
#
# ## Exemplo original com loop for:
# tickets_sold = 0
# max_capacity = 10
# for tickets in range(1, max_capacity + 1):
#     tickets_sold += 1
# print("Sold out:", tickets_sold, "tickets sold!")
#
# Agora, você criará um loop while para realizar a mesma tarefa.

# ## Instruções:
# 1. Crie um loop while para ser executado enquanto `tickets_sold` for menor que `max_capacity`.
# 2. Dentro do loop, incremente `tickets_sold` em 1, representando um aumento para cada ingresso vendido.
# 3. Fora do loop, imprima `tickets_sold`.

# --- Código abaixo ---

tickets_sold = 0
max_capacity = 10

while tickets_sold < max_capacity:
    tickets_sold += 1
    
print("Sold out:", tickets_sold, "tickets sold!")