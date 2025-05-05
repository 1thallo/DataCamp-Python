# Modificação de Variáveis de String

# Enunciado:
# Você se saiu tão bem trabalhando com as avaliações do LLM Camp que eles pediram sua ajuda novamente.
# Eles têm uma variável chamada `most_popular_course`, que contém o nome do curso mais bem classificado.
# No entanto, há problemas com ela:
# 1. Há um erro de digitação. Deveria ser "Introduction" em vez de "Intro".
# 2. Eles querem remover os espaços e usar sublinhados para facilitar a análise.
# 3. Para fins de consistência, eles querem que todos os caracteres sejam minúsculos.

# ## Instruções:
# 1. Atualize a variável de modo que "Intro" passe a ser "Introduction".
# 2. Troque espaços por sublinhados em toda a string contida em `most_popular_course`.
# 3. Atualize o `most_popular_course` para que ele contenha apenas caracteres minúsculos.

# --- Código abaixo ---

# Definição inicial da variável most_popular_course
most_popular_course = "Intro to Embeddings with the OpenAI API"

# Atualização da primeira palavra: "Intro" para "Introduction"
most_popular_course = most_popular_course.replace("Intro", "Introduction")

# Substituição de espaços por sublinhados
most_popular_course = most_popular_course.replace(" ", "_")

# Conversão de todos os caracteres para minúsculas
most_popular_course = most_popular_course.lower()

# Exibição do resultado final no console
print(most_popular_course)