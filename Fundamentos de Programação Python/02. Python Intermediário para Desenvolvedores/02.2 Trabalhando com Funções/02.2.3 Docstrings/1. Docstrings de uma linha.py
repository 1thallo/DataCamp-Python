# Docstrings de uma Linha

# Enunciado:
# Docstrings são usadas para explicar a finalidade de uma função. Embora o nome da função deva ser descritivo,
# isso precisa ser equilibrado com o tamanho do nome da função, por isso as docstrings permitem que você forneça mais detalhes.
#
# Neste exercício, você usará a função `clean_text` criada anteriormente e adicionará uma docstring de linha única.

# ## Instruções:
# 1. Adicione uma docstring informando """Swap spaces to underscores and convert text to lowercase.""".
# 2. Acesse a docstring da função usando o atributo apropriado.

# --- Código abaixo ---

# 1. Definir a função clean_string com uma docstring
def clean_string(text):
    """Swap spaces to underscores and convert text to lowercase."""
    no_spaces = text.replace(" ", "_")
    clean_text = no_spaces.lower()
    return clean_text

# 2. Acessar e imprimir a docstring da função
print(clean_string.__doc__)