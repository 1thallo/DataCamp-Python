"""
Alterando a saída em expressões geradoras

Ótimo! Neste ponto, você já sabe como escrever uma expressão geradora básica. 
Neste exercício, você levará essa ideia um pouco mais longe, adicionando à expressão de saída de uma expressão geradora. 
Como as expressões geradoras e as compreensões de lista são muito parecidas em termos de sintaxe, essa deve ser uma tarefa familiar para você!

Você recebe uma lista de string lannister e, usando uma expressão geradora, cria um objeto gerador que será iterado para imprimir seus valores.

Instruções:
1. Escreva uma expressão geradora que gerará o comprimento de cada string em lannister. Use person como a variável do iterador. 
   Atribua o resultado a lengths.
2. Forneça o iterável correto no loop for para imprimir os valores no objeto gerador.
"""

# --- Código abaixo ---

# Create a list of strings: lannister
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Create a generator object: lengths
lengths = (len(person) for person in lannister)

# Iterate over and print the values in lengths
for value in lengths:
    print(value)