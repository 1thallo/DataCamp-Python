# Evite Erros

# Enunciado:
# No vídeo, você viu algumas abordagens de tratamento de erros que podem ser aplicadas a funções personalizadas.
#
# Neste exercício, você testará uma das abordagens que evita gerar um erro, imprimindo uma mensagem útil
# se ocorrer um erro, mas não encerrando o script.

# ## Instruções:
# 1. Use uma palavra-chave que permita que você tente executar o código que limpa `text`.
# 2. Troque um espaço por um único sublinhado no argumento `text`.
# 3. Use outra palavra-chave que imprima uma mensagem útil se ocorrer um erro ao chamar a função `snake_case()`.

# --- Código abaixo ---

# Definir a função snake_case
def snake_case(text):
    # 1. Tentar limpar o texto
    try:
        # 2. Substituir espaços por sublinhados e converter para minúsculas
        clean_text = text.replace(" ", "_")
        clean_text = clean_text.lower()
    # 3. Executar este código se ocorrer um erro
    except:
        print("The snake_case() function expects a string as an argument, please check the data type provided.")

# Chamar a função com um exemplo válido
snake_case("User Name 187")