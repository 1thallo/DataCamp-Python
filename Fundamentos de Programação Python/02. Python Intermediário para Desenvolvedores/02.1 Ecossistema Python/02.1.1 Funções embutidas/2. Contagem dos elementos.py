# Contagem dos Elementos

# Enunciado:
# Neste exercício, você usará uma das funções embutidas mais úteis do Python para contar o número de elementos
# em diferentes tipos de variáveis.
#
# Você trabalhará com três variáveis:
# - `course_ratings`: um dicionário que contém os nomes dos cursos como chaves e as notas médias como valores.
# - `course_completions`: uma lista que contém o número diário de conclusões de um curso individual.
# - `most_popular_course`: uma string que contém o nome de um curso.
#
# Seu objetivo é aplicar a função `len()` para contar os elementos em cada uma dessas variáveis.

# ## Instruções:
# 1. Use a função `len()` para contar o número de pares de valor-chave em `course_ratings`, armazenando-os como `num_courses` e imprimindo a variável.
# 2. Use a função `len()` para contar o número de elementos em `course_completions`, armazenando como `num_courses` e imprimindo a variável.
# 3. Use a função `len()` para contar o número de caracteres em `most_popular_course`, armazenando como `title_length` e imprimindo a variável.

# --- Código abaixo ---

# 1. Contar o número de pares de valor-chave em course_ratings
course_ratings = {
    "LLM Concepts": 4.7,
    "Introduction to Data Pipelines": 4.75,
    "AI Ethics": 4.62,
    "Introduction to dbt": 4.81
}

# Número de cursos no dicionário
num_courses = len(course_ratings)
print(num_courses)

# 2. Contar o número de elementos em course_completions
course_completions = [97, 83, 121, 205, 56, 174, 92, 117, 164]

# Número de cursos na lista
num_courses = len(course_completions)
print(num_courses)

# 3. Contar o número de caracteres em most_popular_course
most_popular_course = "Introduction to dbt"

# Comprimento do título do curso
title_length = len(most_popular_course)
print(title_length)