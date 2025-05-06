"""
Uso de condicionais em compreensões (1)

Você tem usado compreensões de lista para criar listas de valores, às vezes usando operações para criar esses valores.

Um mecanismo interessante nas compreensões de lista é que você também pode criar listas com valores que atendam apenas a uma determinada condição. 
Uma maneira de fazer isso é usar condicionais nas variáveis do iterador. Neste exercício, você fará exatamente isso.

Lembre-se de que, no vídeo, você pode aplicar uma instrução condicional para testar a variável do iterador adicionando uma instrução if 
na parte da expressão de predicado opcional após a instrução for na compreensão:

[ expressão de saída for variável de iterador in iterável if expressão de predicado ].

Você usará essa receita para escrever uma compreensão de lista para este exercício. 
Você receberá uma lista de strings fellowship e, usando uma compreensão de lista, criará uma lista que inclua apenas os membros de fellowship 
que tenham 7 caracteres ou mais.

Instruções:
1. Use member como a variável do iterador na compreensão da lista. 
2. Para a condicional, use len() para avaliar a variável do iterador. 
   Observe que você deseja apenas strings com 7 caracteres ou mais.
"""

# --- Código abaixo ---

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member) >= 7]

# Print the new list
print(new_fellowship)