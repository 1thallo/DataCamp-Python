# Limpeza de Dados de Texto

# Enunciado:
# No vídeo, você viu como criar uma função personalizada que executa um cálculo e arredonda os resultados.
# No entanto, as funções personalizadas podem ser usadas para qualquer tarefa que pretendemos repetir!
# Um exemplo comum é a limpeza de dados de texto para que estejam em conformidade com requisitos específicos.
#
# Neste exercício, você criará uma função que recebe dados de strings e:
# - Substitui espaços por sublinhados.
# - Converte para letras minúsculas.
# - Retorna a string formatada.

# ## Instruções:
# 1. Defina uma função chamada `clean_string`, que recebe um argumento chamado `text`.
# 2. Dentro da função, crie uma variável chamada `no_spaces`, que contém `text` com espaços substituídos por sublinhados.
# 3. Dentro da função, crie uma variável chamada `clean_text`, que converte os caracteres em `no_spaces` para minúsculas.
# 4. Conclua a função produzindo `clean_text` como saída.

# --- Código abaixo ---

def clean_string(text):
    no_spaces = text.replace(" ", "_")
    clean_text = no_spaces.lower()
    return clean_text

converted_text = clean_string("I LoVe dATaCamP!")
print(converted_text)