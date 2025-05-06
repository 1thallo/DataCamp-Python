"""
Uso de condicionais em compreensões (2)

No exercício anterior, você usou uma instrução condicional if na parte da expressão de predicado de uma compreensão de lista 
para avaliar uma variável de iterador. Neste exercício, você usará uma instrução if-else na expressão de saída da lista.

Você trabalhará na mesma lista, fellowship e, usando uma compreensão de lista e uma instrução condicional if-else na expressão de saída, 
criará uma lista que mantenha os membros de fellowship com 7 ou mais caracteres e substitua os outros por uma string vazia. 
Use member como a variável do iterador na compreensão da lista.

Instruções:
1. Na expressão de saída, mantenha a string como está se o número de caracteres for >= 7; 
   caso contrário, substitua-a por uma string vazia, ou seja, '' ou "".
"""

# --- Código abaixo ---

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member if len(member) >= 7 else '' for member in fellowship]

# Print the new list
print(new_fellowship)