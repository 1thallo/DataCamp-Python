# Mercado de Aluguel

# Enunciado:
# Você está querendo se mudar e definiu variáveis contendo seus requisitos/limites de número de quartos,
# área mínima e aluguel máximo:
#
# min_num_beds = 2
# min_sq_foot = 750
# max_rent = 1900
#
# Você viu uma propriedade na qual se interessou e armazenou suas informações nas variáveis
# `num_beds`, `sq_foot` e `rent`. Você criará um fluxo de trabalho personalizado para verificar
# se essa propriedade em potencial atende às suas necessidades.

# --- Código abaixo ---

# Check the number of beds
if num_beds < min_num_beds:
  print("Insufficient bedrooms")

# Check square feet
elif sq_foot <= min_sq_foot:
  print("Too small")
  
# Check the rent
elif rent > max_rent:
    print("Too expensive")

# If all conditions met
else:
  print("This looks promising!")