"""
Divisão com números inteiros e de ponto flutuante

O Python oferece suporte a dois operadores de divisão diferentes: / e //. 
No Python 3, / retornará consistentemente um resultado float, e // é a divisão inteira e retornará consistentemente um resultado inteiro. 
A divisão inteira é o mesmo que fazer math.floor(numerator/divisor), que retorna o maior número inteiro menor ou igual ao resultado da operação de divisão.
"""

# --- Código abaixo ---

# Print the result of 2/1 and 1/2
print(2/1)
print(1/2)

# Print the floored division result of 2//1 and 1//2
print(2//1)
print(1//2)

# Print the type of 2/1 and 2//1
print(type(2/1))
print(type(2//1))