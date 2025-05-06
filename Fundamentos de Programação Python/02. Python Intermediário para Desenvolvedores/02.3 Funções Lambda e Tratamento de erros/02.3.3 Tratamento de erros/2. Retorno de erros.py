# Retorno de Erros

# Enunciado:
# É hora de experimentar a outra abordagem para o tratamento de erros.
#
# Edite a função `snake_case()` para produzir intencionalmente um erro se um tipo de dados incorreto for usado.

# ## Instruções:
# 1. Verifique se o tipo de dados do argumento `text` é string (`str`).
# 2. Dentro do bloco `else`, produza um `TypeError()` para impedir a execução do script e retornar uma mensagem descritiva.

# --- Código abaixo ---

# Definir a função snake_case
def snake_case(text):
    # 1. Verificar o tipo de dado
    if type(text) == str:
        clean_text = text.replace(" ", "_")
        clean_text = clean_text.lower()
    else:
        # 2. Retornar um erro TypeError se o tipo de dado estiver incorreto
        raise TypeError("The snake_case() function expects a string as an argument, please check the data type provided.")

snake_case("User Name 187")