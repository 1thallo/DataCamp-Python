"""
Criação de dicionários de estrutura desconhecida

Ocasionalmente, você precisará de uma estrutura para armazenar dados aninhados, e talvez não tenha certeza se todas as chaves realmente existem. 
Isso pode ser um problema se você estiver tentando anexar itens a uma lista para essa chave. 
Você deve se lembrar dos dados de NYC que exploramos no vídeo. 
Para resolver o problema com um dicionário normal, você precisará testar se a chave existe no dicionário e, se não existir, adicioná-la com uma lista vazia.

Você vai trabalhar com uma lista de entradas que contém espécies, comprimento das nadadeiras, massa corporal e sexo dos pinguins fêmeas do nosso estudo. 
Você vai resolver esse mesmo tipo de problema com uma solução muito mais fácil no próximo exercício.
"""

# --- Código abaixo ---

# Create an empty dictionary: female_penguin_weights
female_penguin_weights = {}

# Iterate over the weight_log entries
for species, sex, body_mass in weight_log:
    # Check to see if species is already in the dictionary
    if species not in female_penguin_weights:
        # Create an empty list for any missing species
        female_penguin_weights[species] = []
    # Append the sex and body_mass as a tuple to the species keys list
    female_penguin_weights[species].append((sex, body_mass))
    
# Print the weights for 'Adlie'
print(female_penguin_weights['Adlie'])