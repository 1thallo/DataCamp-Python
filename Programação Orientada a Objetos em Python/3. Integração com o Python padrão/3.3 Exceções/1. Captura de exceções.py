"""
Captura de exceções
Antes de começar a escrever suas próprias exceções personalizadas, vamos nos certificar de que você conhece os conceitos básicos de tratamento de exceções.

Neste exercício, você receberá uma função invert_at_index(x, ind) que recebe dois argumentos, uma lista x e um índice ind, e inverte o elemento da lista nesse índice. Por exemplo, invert_at_index([5,6,7], 1) retorna 1/6, ou 0.166666.

Tente executar o código como está e examine a saída no console. Há duas operações inseguras nessa função: primeiro, se o elemento que estivermos tentando inverter tiver o valor 0, o código causará uma exceção ZeroDivisionError. Segundo, se o índice passado para a função estiver fora do intervalo da lista, o código causará um IndexError. Em ambos os casos, o script será interrompido, o que pode não ser desejável.

Instruções
Use a try - except - except pattern (with two except blocks) inside the function to catch and handle two exceptions as follows:

try executar o código como está,
Se ocorrer ZeroDivisionError, imprima "Cannot divide by zero!",
Se ocorrer IndexError, imprima "Index out of range!"
"""

# resposta:
# MODIFY the function to catch exceptions
def invert_at_index(x, ind):
    try:
        return 1/x[ind]
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except IndexError:
        print("Index out of range!")
    
 
a = [5,6,0,7]

# Works okay
print(invert_at_index(a, 1))

# Potential ZeroDivisionError
print(invert_at_index(a, 2))

# Potential IndexError
print(invert_at_index(a, 5))
