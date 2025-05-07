"""
Verificação de dados nos dicionários

Você pode verificar se uma chave existe em um dicionário usando a expressão in.

Por exemplo, você pode verificar se 'cookies' é uma chave no dicionário recipes usando if 'cookies' in recipes:. 
Isso permite que você reaja com segurança à presença de dados no dicionário.

Carregamos um dicionário squirrels_by_park com nomes de parques para as chaves e uma lista de dicionários dos esquilos.
"""

# --- Código abaixo ---

# Check to see if Tompkins Square Park is in squirrels_by_park
if "Tompkins Square Park" in squirrels_by_park:
    # Print 'Found Tompkins Square Park'
    print('Found Tompkins Square Park')
    
# Check to see if Central Park is in squirrels_by_park
if "Central Park" in squirrels_by_park:
    # Print 'Found Central Park' if found
    print('Found Central Park')
else:
    # Print 'Central Park missing' if not found
    print('Central Park missing')