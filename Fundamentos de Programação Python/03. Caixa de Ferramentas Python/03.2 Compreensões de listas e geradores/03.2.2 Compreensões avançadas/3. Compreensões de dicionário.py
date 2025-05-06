"""
Compreensões de dicionário

As compreensões não são relegadas apenas ao mundo das listas. Há muitos outros objetos que você pode criar usando compreensões, 
como dicionários, objetos comuns na ciência de dados. Você criará um dicionário usando a sintaxe de compreensão para este exercício. 
Nesse caso, a compreensão é chamada de compreensão de dicionário.

Lembre-se de que a principal diferença entre uma compreensão de lista e uma compreensão de dicionário é o uso de chaves {} em vez de []. 
Além disso, os membros do dicionário são criados usando dois pontos :, como em <key> : <value>.

Você recebe uma lista de strings fellowship e, usando uma compreensão de dicionário, cria um dicionário com os membros da lista como chaves 
e o comprimento de cada string como os valores correspondentes.

Instruções:
1. Crie uma compreensão de dicionário em que a chave é uma string em fellowship e o valor é o comprimento da string. 
   Lembre-se de usar a sintaxe <key> : <value> na parte da expressão de saída da compreensão para criar os membros do dicionário. 
   Use member como a variável do iterador.
"""

# --- Código abaixo ---

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create dict comprehension: new_fellowship
new_fellowship = {member: len(member) for member in fellowship}

# Print the new dictionary
print(new_fellowship)