# Verificação de Tipos de Dados

# Enunciado:
# O Python facilita nossa vida ao inferir o tipo de dados das variáveis com as quais você trabalha,
# evitando a necessidade de declarar o tipo de dados explicitamente.

# ## Cenário:
# Vamos praticar a verificação do tipo de dados de diferentes valores e variáveis.
# Você tem três variáveis: `customer_age`, `account_balance`, e `is_millionaire`,
# e aprenderá a obter seus tipos de dados.

# --- Código abaixo ---

# Definição da variável customer_age como um número inteiro
customer_age = 49

# Exibição do tipo de dado da variável customer_age
print(type(customer_age))  # Deve exibir <class 'int'>

# Definição da variável account_balance como um número decimal
account_balance = 120078.89

# Exibição do tipo de dado da variável account_balance
print(type(account_balance))  # Deve exibir <class 'float'>

# Definição da variável is_millionaire como um valor booleano
is_millionaire = False

# Exibição do tipo de dado da variável is_millionaire
print(type(is_millionaire))  # Deve exibir <class 'bool'>