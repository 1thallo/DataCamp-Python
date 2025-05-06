# Adicionar Argumento de Palavra-Chave

# Enunciado:
# Anteriormente, você desenvolveu uma função personalizada para limpar o texto, como mostrado aqui:
#
# # Create the clean_string function
# def clean_string(text):
#       # Replace spaces with underscores
#       no_spaces = text.replace(" ", "_")
#       # Convert to lowercase
#       clean_text = no_spaces.lower()
#       # Display the final text as an output
#       return clean_text
#
# Agora, você vai modificá-la para receber diferentes argumentos de palavras-chave padrão!

# ## Instruções 1/2:
# Defina `clean_text`, que tem dois argumentos: `text`, e `lower`, sendo que o último tem um valor padrão de `True`.

# --- Código para Instrução 1 ---
# Define clean_text
def clean_text(text, lower=True):
    if lower == False:
        clean_text = text.replace(" ", "_")
        return clean_text
    else:
        clean_text = text.replace(" ", "_")
        clean_text = clean_text.lower()
        return clean_text

# ## Instruções 2/2:
# Redefina `clean_text` com argumentos de `text` seguidos de `remove`, com o último tendo um valor padrão de `None`.

# --- Código para Instrução 2 ---
# Define clean_text
def clean_text(text, remove=None):
    if remove != None:
        clean_text = text.replace(remove, "")
        clean_text = clean_text.lower()
        return clean_text
    else:
        clean_text = text.lower()
        return clean_text