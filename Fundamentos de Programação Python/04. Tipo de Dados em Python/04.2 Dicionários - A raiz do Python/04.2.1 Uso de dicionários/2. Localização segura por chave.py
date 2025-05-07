"""
Localização segura por chave

Conforme demonstrado no vídeo, se você tentar acessar uma chave que não está presente em um dicionário, receberá um KeyError. 
Uma opção para lidar com esse tipo de erro é usar um bloco try: except:. 
O Python oferece uma ferramenta mais rápida e versátil para ajudar você com esse problema na forma do método .get(). 
O método .get() permite que você forneça o nome de uma chave e, opcionalmente, o que você deseja que seja retornado se a chave não for encontrada.

Você usará o mesmo dicionário squirrels_by_park, que tem como chave o nome do parque e o valor é uma tupla com a cor principal, 
os destaques, a ação e a reação aos seres humanos, e ganhará prática usando o método .get().
"""

# --- Código abaixo ---

# Safely print 'Union Square Park' from the squirrels_by_park dictionary
print(squirrels_by_park.get('Union Square Park'))

# Safely print the type of 'Fort Tryon Park' from the squirrels_by_park dictionary
print(type(squirrels_by_park.get('Fort Tryon Park')))

# Safely print 'Central Park' from the squirrels_by_park dictionary or 'Not Found'
print(squirrels_by_park.get('Central Park', 'Not Found'))