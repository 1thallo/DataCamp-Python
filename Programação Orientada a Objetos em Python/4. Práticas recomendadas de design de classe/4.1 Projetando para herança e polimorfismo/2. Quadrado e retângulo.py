"""
Quadrado e retângulo

O exemplo clássico de um problema que viola o Princípio de Substituição de Liskov é o problema do Círculo-Elipse,
às vezes chamado de problema do Quadrado-Retângulo.

De qualquer forma, parece que você deve ser capaz de definir uma classe Rectangle, com atributos h e w (para altura e largura)
e, em seguida, definir uma classe Square que herda da Rectangle. Afinal de contas, um quadrado "é" um retângulo!

Infelizmente, essa intuição não se aplica ao design orientado a objetos.

Instruções 1/4
Crie uma classe Rectangle com um construtor que aceite dois parâmetros, h e w,
e defina seus atributos h e w com os valores de h e w.
Crie uma classe Square herdada de Rectangle com um construtor que aceite um parâmetro w
e defina os atributos h e w como o valor de w.
"""

# resposta instrucao 1:
# Define a Rectangle class
class Rectangle:
    def __init__(self, h, w):
        self.h = h
        self.w = w

# Define a Square class
class Square(Rectangle):
    def __init__(self, w):
        self.h = w
        self.w = w
"""
--------------------------------------------------------------
                   Quadrado e Retângulo - Instruções 2/4
--------------------------------------------------------------

As classes Rectangle e Square já foram definidas para você. Agora, realize testes com elas no console ou 
no painel de script, como indicado a seguir.

Passo 1: Crie um objeto da classe Square com comprimento lateral 4.
Passo 2: Tente atribuir o valor 7 ao atributo h desse objeto.

Pergunta:
O que deu errado com essas classes?

Respostas possíveis:

1) "Esse não foi um uso correto da herança: não chamamos o construtor pai no construtor filho."
2) "Não podemos definir o atributo h como 7 no objeto Square porque isso causará um erro."
3) "RESPOSTA CERTA: O objeto Square 4x4 deixaria de ser um quadrado se atribuíssemos 7 a h."
4) "Como um Square tem apenas um comprimento lateral, ele não deve ter o atributo h. Não deveríamos ter incluído o atributo h no construtor."
5) "Todas as opções acima."

--------------------------------------------------------------
"""

"""
--------------------------------------------------------------
                   Quadrado e Retângulo - Instruções 3/4
--------------------------------------------------------------

Para garantir que os atributos h e w de um Square (herdado de Rectangle) não possam ser alterados de forma independente, 
devemos implementar métodos que alterem ambos os atributos simultaneamente.

Passos:
1) Defina os métodos `set_h()` e `set_w()` na classe Rectangle. Cada um desses métodos deve aceitar um parâmetro e 
   configurar os atributos h e w.
   
2) Em seguida, defina os métodos `set_h()` e `set_w()` na classe Square. Cada um desses métodos deve aceitar um parâmetro 
   e atualizar tanto h quanto w para esse valor, garantindo que eles sejam sempre iguais.

--------------------------------------------------------------
"""
class Rectangle:
    def __init__(self, w, h):
        self.w, self.h = w, h

    # Define set_h to set h      
    def set_h(self, h):
        self.h = h

    # Define set_w to set w          
    def set_w(self, w):
        self.w = w


class Square(Rectangle):
    def __init__(self, w):
        self.w, self.h = w, w

    # Define set_h to set w and h
    def set_h(self, h):
        self.h = h
        self.w = h

    # Define set_w to set w and h      
    def set_w(self, w):
        self.w = w
        self.h = w



# Instruções 4/4

# Pergunta
# Mais adiante neste capítulo, você aprenderá como fazer com que esses métodos setter sejam executados automaticamente quando novos valores forem atribuídos aos atributos. Por enquanto, não se preocupe com isso, apenas suponha que, quando atribuirmos um valor a h de um quadrado, o atributo w será alterado de acordo.

# Como o uso desses métodos de configuração viola o princípio da substituição de Liskov?

# Respostas possíveis

# Há inconsistências sintáticas.

# RESPOSTA CERTA >> Cada um dos métodos setter de Square altera os atributos de h e w, enquanto os métodos setter de Rectangle alteram apenas um atributo por vez, de modo que os objetos Square não podem ser substituídos por Rectangle em programas que dependem da manutenção de um atributo constante.

# Os métodos setter de Square aceitam apenas um intervalo limitado de parâmetros, ao contrário dos métodos setter de Rectangle, de modo que os objetos Square não podem ser substituídos por Rectangle em programas que usam valores de parâmetros fora desse intervalo.

# Todas as opções acima.
