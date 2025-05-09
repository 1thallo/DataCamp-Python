"""
Projeto: Criar Funções para Registrar Usuários no App

Objetivo:
1. Criar uma função validate_user() para validar os dados de entrada do usuário.
2. Criar uma função register_user() para lidar com a lógica de registro.

Detalhes:
- validate_user():
  - Recebe os parâmetros: name, email, e password.
  - Chama funções auxiliares de validação: validate_name(), validate_email(), e validate_password().
  - Levanta um ValueError com uma mensagem descritiva se alguma validação falhar.
  - Retorna True se todas as validações passarem.

- register_user():
  - Recebe os parâmetros: name, email, e password.
  - Chama validate_user() para validar os dados do usuário.
  - Retorna False se validate_user() levantar um ValueError.
  - Caso contrário, cria e retorna um dicionário com os dados do usuário.
"""

# Start coding here
# Use as many cells as you need
def validate_user(name, email, password):
    if validate_name(name) == False:
        raise ValueError("O nome deve ser maior que 2 caracteres!")

    if validate_email(email) == False:
        raise ValueError("Formato de email incorreto!")

    if validate_password(password) == False:
        raise ValueError("Senha muito fraca, coloque numeros e letras maiusculas!")

    return True

def register_user(name, email, password):
    try:
        validate_user(name, email, password)
    except:
        return False

    user = {"name": name, "email": email, "password": password}

    return user