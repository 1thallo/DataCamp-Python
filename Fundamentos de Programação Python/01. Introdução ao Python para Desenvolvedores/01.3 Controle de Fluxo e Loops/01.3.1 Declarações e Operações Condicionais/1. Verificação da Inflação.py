# Verificação da Inflação

# Enunciado:
# O governo do UK solicitou sua ajuda na análise das estatísticas de inflação.
# Eles forneceram a você os dados de setembro e agosto de 2023 armazenados como duas variáveis float,
# `inflation_september` e `inflation_august`, respectivamente.
# Você precisará criar um fluxo de trabalho que compare essas estatísticas.

# ## Instruções:
# 1. Verifique se `inflation_september` é menor que `inflation_august`, imprimindo "Inflation decreased" se esse for o caso.
# 2. Caso contrário, verifique se `inflation_september` é maior que `inflation_august`, imprimindo "Inflation increased" se for verdadeiro.
# 3. Caso contrário, imprima "Inflation remained stable".

# --- Código abaixo ---

# 1. Verificar se a inflação de setembro é menor que a de agosto
if inflation_september < inflation_august:
    print("Inflation decreased") 

# 2. Verificar se a inflação de setembro é maior que a de agosto
elif inflation_september > inflation_august:
    print("Inflation increased")  

# 3. Caso contrário, as inflações são iguais
else:
    print("Inflation remained stable") 