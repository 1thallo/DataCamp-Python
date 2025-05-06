# Fazendo Cálculos

# Enunciado:
# As funções embutidas do Python facilitam a realização de cálculos com muitos valores sem que você precise
# escrever várias linhas de código.
#
# Trabalhando com uma lista chamada `course_completions` que contém valores inteiros que representam o número
# de conclusões de uma série de cursos diferentes, você analisará esses dados para obter insights!

# --- Código abaixo ---

# Lista de conclusões de cursos
course_completions = [97, 83, 121, 205, 56, 174, 92, 117, 164]

# ## Instruções 1/4:
# Some e imprima o número total de course_completions.
# Resposta:
print(sum(course_completions))

# ## Instruções 2/4:
# Imprima o maior valor em course_completions.
# Resposta:
print(max(course_completions))

# ## Instruções 3/4:
# Some os valores em course_completions e, em seguida, divida-os pelo número de elementos para obter a média.
# Resposta:
print(sum(course_completions) / len(course_completions))

# ## Instruções 4/4:
# Arredonde o número médio de conclusões de curso para uma casa decimal.
# Resposta:
print(round(sum(course_completions) / len(course_completions), 1))