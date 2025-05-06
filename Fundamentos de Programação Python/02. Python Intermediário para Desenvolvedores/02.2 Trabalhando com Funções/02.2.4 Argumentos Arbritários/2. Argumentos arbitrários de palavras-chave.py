# Argumentos Arbitrários de Palavras-Chave

# Enunciado:
# Argumentos posicionais arbitrários são uma maneira de adicionar flexibilidade ao criar funções personalizadas,
# mas você também pode usar argumentos arbitrários de palavras-chave.
#
# Seu objetivo é usar a função `concat` que você criou no último exercício e modificá-la para aceitar argumentos
# arbitrários de palavras-chave.

# ## Instruções:
# 1. Defina `concat()` como uma função que aceita argumentos de palavras-chave arbitrárias chamadas `kwargs`.
# 2. Dentro da função, crie uma string vazia.
# 3. Dentro da função, faça um loop sobre os valores do argumento da palavra-chave, usando `kwarg` como iterador.
# 4. Chame `concat()` com argumentos de palavra-chave de `start` igual a "Python", `middle` igual a "is" e `end` igual a "great!".

# --- Código abaixo ---

def concat(**kwargs):
    result = ""
    
    for kwarg in kwargs.values():
        result += " " + kwarg
    return result

print(concat(start="Python", middle="is", end="great!"))