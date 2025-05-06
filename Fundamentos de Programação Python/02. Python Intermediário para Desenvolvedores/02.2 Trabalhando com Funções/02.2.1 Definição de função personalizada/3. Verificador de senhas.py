# Verificador de Senhas

# Enunciado:
# Você viu como as instruções condicionais podem ser usadas para verificar a igualdade.
# Agora que você tem as habilidades para criar uma função personalizada, combinará essas duas técnicas
# para criar uma função chamada `password_checker` que compara a senha de um usuário a um valor enviado,
# imprimindo condicionalmente uma saída dependendo do resultado.

# ## Instruções:
# 1. Defina a função `password_checker`, que deve aceitar um argumento chamado `submission`.
# 2. Verifique se `password` é igual a `submission`.
# 3. Adicione uma palavra-chave que permita a impressão condicional de "Incorrect password" se `password` e `submission` forem diferentes.
# 4. Chame a função, passando "NOT_VERY_SECURE_2023".

# --- Código abaixo ---

# Senha correta
password = "not_very_secure_2023"

def password_checker(submission):
    if password == submission:
        print("Successful login!")
    else:
        print("Incorrect password")

password_checker("NOT_VERY_SECURE_2023")