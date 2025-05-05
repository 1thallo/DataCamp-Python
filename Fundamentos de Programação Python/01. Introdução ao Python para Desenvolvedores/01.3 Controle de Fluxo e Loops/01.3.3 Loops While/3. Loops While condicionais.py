# Loops While Condicionais

# Enunciado:
# Você se ofereceu para ajudar a criar um programa que o LLM Camp possa usar para promover um novo curso
# que será lançado no dia 26 do mês.
#
# A data de hoje é 22, e eles têm uma versão de pré-lançamento disponível a partir do dia 24
# para todos os usuários que comprarem uma assinatura até o dia 24!
#
# Você precisará criar um fluxo de trabalho personalizado que forneça mensagens personalizadas, dependendo da data.

# ## Instruções:
# 1. Crie um loop while com base no fato de `current_date` ser menor ou igual a `release_date`.
# 2. Verifique se `current_date` é menor ou igual a 24 e, em caso afirmativo, imprima
#    "Purchase before the 25th for early access".
# 3. Caso contrário, verifique se `current_date` é igual a 25, imprimindo "Coming soon!".
# 4. Após todas as verificações, incremente `current_date` em um para cada dia que passar.

# --- Código abaixo ---

# Data de lançamento do curso
release_date = 26

# Data atual
current_date = 22

# Loop condicional enquanto current_date for menor ou igual a release_date
while current_date <= release_date:
    # Promover compras antes do dia 25
    if current_date <= 24:
        print("Purchase before the 25th for early access")
    # Verificar se a data é igual ao dia 25
    elif current_date == 25:
        print("Coming soon!")
    # Caso contrário, o curso já está disponível
    else:
        print("Available now!")
    
    # Incrementar current_date em 1 para simular a passagem dos dias
    current_date += 1