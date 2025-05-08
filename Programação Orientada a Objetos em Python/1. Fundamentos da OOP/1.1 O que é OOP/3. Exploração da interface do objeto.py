"""
Exploração da interface do objeto

A melhor maneira de aprender a escrever código orientado a objetos é estudar o design das classes existentes. 
Você já aprendeu sobre ferramentas de exploração como type() e dir().

Outra função importante é help(): chamar help(x) no console mostrará a documentação do objeto ou da classe x.

A maioria das classes do mundo real tem muitos métodos e atributos, e é fácil se perder. 
Sendo assim, neste exercício, você começará com algo mais simples. Definimos uma classe e criamos um objeto dessa classe chamado mystery. 
Explore o objeto no console usando as ferramentas que aprendeu.

Instruções:
- Imprima o atributo name do funcionário mystery.
- Imprima o salário do funcionário.
- Dê à Natasha (funcionária mystery) um aumento de US$ 2.500 usando um método apropriado.
- Imprima o salário novamente após o aumento.
"""

# -- Código --

# Print the mystery employee's name
print(mystery.name)

# Print the mystery employee's salary
print(mystery.salary)

# Give the mystery employee a raise of $2500
mystery.give_raise(2500)

# Print the salary again
print(mystery.salary)
