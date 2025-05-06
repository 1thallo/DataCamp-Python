"""
Compreensões de listas aninhadas

Ótimo! Neste ponto, você já tem uma boa noção da sintaxe básica das compreensões de lista. 
Vamos aprimorar um pouco mais suas habilidades de programação. 
Neste exercício, você escreverá uma compreensão de lista dentro de outra compreensão de lista, ou compreensões de lista aninhadas.

Vamos deixar as strings de lado por um tempinho. 
Uma das maneiras pelas quais as listas podem ser usadas é na representação de objetos multidimensionais, como matrizes. 
Em Python, as matrizes podem ser representadas como uma lista de listas. Por exemplo, uma matriz 5 x 5 com valores 0 a 4 em cada linha pode ser escrita como:

matrix = [[0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4]]

Sua tarefa é recriar essa matriz usando compreensões de lista aninhadas. 
Lembre-se de que você pode criar uma das linhas da matriz com uma única compreensão de lista. 
Para criar a lista de listas, você só precisa fornecer a compreensão de lista como a expressão de saída da compreensão de lista geral:

[[expressão de saída] for variável do iterador in iterável]

Instruções:
1. Na compreensão de lista interna, ou seja, a expressão de saída da compreensão de lista aninhada, 
   crie uma lista de valores de 0 a 4 usando range(). Use col como a variável do iterador.
2. Na parte iterável de sua compreensão de lista aninhada, use range() para contar 5 linhas, ou seja, crie uma lista de valores de 0 a 4. 
   Use row como a variável do iterador; observe que você não precisará dessa variável para criar valores na lista de listas.
"""

# --- Código abaixo ---

# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(0, 5)] for row in range(5)]

# Print the matrix
for row in matrix:
    print(row)