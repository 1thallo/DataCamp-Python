# Adicionando Argumentos Arbitrários

# Enunciado:
# No vídeo, você viu que o Python permite que as funções personalizadas aceitem qualquer número de argumentos
# posicionais por meio do uso de "argumentos arbitrários". Essa flexibilidade permite que as funções sejam usadas
# de várias maneiras e ainda produzam os resultados esperados!
#
# Usando esse poder, você criará uma função que concatena (une) strings, independentemente de quantos blocos
# de texto forem fornecidos!

# ## Instruções:
# 1. Defina uma função chamada `concat()` que aceite argumentos arbitrários chamados `args`.
# 2. Crie uma variável chamada `result` e atribua a ela uma string vazia.
# 3. Use um loop for para iterar sobre cada `arg` em `args`.
# 4. Chame a função para testar se ela está funcionando corretamente.

# --- Código abaixo ---

# 1. Definir a função chamada concat
def concat(*args):
    # 2. Criar uma string vazia
    result = ""
    
    # 3. Iterar sobre os argumentos fornecidos
    for arg in args:
        result += " " + arg
    return result

# 4. Chamar a função e testar
print(concat("Python", "is", "great!"))