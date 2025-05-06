"""
Escreva suas próprias expressões geradoras

Você já sabe o que são geradores e expressões geradoras, bem como a diferença entre eles e as compreensões de lista. 
Neste exercício, você praticará a criação de expressões geradoras por conta própria.

Lembre-se de que as expressões geradoras têm basicamente a mesma sintaxe das compreensões de lista, 
exceto pelo uso de parênteses () em vez de colchetes []; assim fica fácil se lembrar! 
Além disso, se você já iterou em um dicionário com .items() ou usou a função range(), por exemplo, 
já encontrou e usou geradores antes, sem saber. Quando você usa essas funções, o Python cria geradores para você nos bastidores.

Agora, você começará de forma simples, criando um objeto gerador que produz valores numéricos.

Instruções:
1. Crie um objeto gerador que produzirá valores de 0 a 30. Atribua o resultado a result e use num como a variável do iterador na expressão do gerador.
2. Imprima os primeiros valores de 5 usando next() apropriadamente em print().
3. Imprima o restante dos valores usando um loop for para iterar sobre o objeto gerador.
"""

# --- Código abaixo ---

# Create generator object: result
result = (num for num in range(0, 31))

# Print the first 5 values
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

# Print the rest of the values
for value in result:
    print(value)