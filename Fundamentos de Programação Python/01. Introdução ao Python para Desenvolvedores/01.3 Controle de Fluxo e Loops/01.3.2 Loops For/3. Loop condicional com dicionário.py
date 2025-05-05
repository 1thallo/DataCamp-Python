# Loop Condicional com um Dicionário

# Enunciado:
# Seu amigo do LLM Camp forneceu a você um dicionário chamado `courses`. Ele contém os nomes dos cursos como chaves
# e o tópico associado a eles como um valor. Há três tópicos: "AI", "Programming", e "Data Engineering".
#
# courses = {
#     "LLM Concepts": "AI",
#     "Introduction to Data Pipelines": "Data Engineering",
#     "AI Ethics": "AI",
#     "Introduction to dbt": "Data Engineering",
#     "Writing Efficient Python Code": "Programming",
#     "Introduction to Docker": "Programming"
# }
#
# Essa é uma ótima oportunidade para você praticar o loop nos dicionários!

# ## Instruções:
# 1. Crie um loop for para iterar sobre `key, value` em `courses.items()`.
# 2. Verifique se `value` é "AI" e, se for o caso, imprima `key`.
# 3. Caso contrário, verifique se `value` é "Programming", imprimindo a `key` se for o caso.
# 4. Caso contrário, imprima a `key` para confirmar que se trata de um curso de "Data Engineering".

# --- Código abaixo ---

courses = {
    "LLM Concepts": "AI",
    "Introduction to Data Pipelines": "Data Engineering",
    "AI Ethics": "AI",
    "Introduction to dbt": "Data Engineering",
    "Writing Efficient Python Code": "Programming",
    "Introduction to Docker": "Programming"
}

# Código-resposta:
for key, value in courses.items():
    if value == "AI":
        print(key, "is an AI course")
    elif value == "Programming":
        print(key, "is a Programming course")
    else:
        print(key, "is a Data Engineering course")