"""
Escrevendo compreensões de listas

Agora você tem todo o conhecimento necessário para começar a escrever compreensões de listas! 
Sua tarefa neste exercício é escrever uma compreensão de lista que produz uma lista dos quadrados dos números que variam de 0 a 9.

Instruções:
1. Usando o intervalo de números de 0 a 9 como iterável e i como variável de iterador, 
   escreva uma compreensão de lista que produza uma lista de números consistindo nos valores de i ao quadrado.
"""

# --- Código abaixo ---

# Create list comprehension: squares
squares = [i**2 for i in range(0, 10)]

# Print the result
print(squares)