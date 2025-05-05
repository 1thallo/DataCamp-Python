# Sets de DJs

# Enunciado:
# Para praticar o trabalho com estruturas de dados, você decide dividir os artistas da sua playlist por gênero musical,
# o que lhe permite criar conjuntos para cada gênero.
# Neste exercício, você criará um conjunto para conter artistas independentes e converterá uma lista de artistas de hip-hop em um conjunto.

# ## Instruções:
# 1. Crie um conjunto chamado `indie_set` contendo "Kings of Leon", "Arctic Monkeys" e "Stereophonics".
# 2. Converta a lista `hip_hop` em um conjunto, salvando-a como uma nova variável chamada `hip_hop_set`.
# 3. Imprima as variáveis de conjunto `indie_set` e `hip_hop_set`.

# --- Código abaixo ---

# Lista de artistas de hip-hop
hip_hop = ["Drake", "JAY-Z", "50 Cent", "Drake"]  # "Drake" aparece duas vezes

# 1. Criação do conjunto indie_set
indie_set = {"Kings of Leon", "Arctic Monkeys", "Stereophonics"}

# 2. Conversão da lista hip_hop para um conjunto
hip_hop_set = set(hip_hop)  # Remove duplicatas automaticamente

# 3. Impressão dos conjuntos indie_set e hip_hop_set
print("Indie Set:", indie_set)
print("Hip-Hop Set:", hip_hop_set)