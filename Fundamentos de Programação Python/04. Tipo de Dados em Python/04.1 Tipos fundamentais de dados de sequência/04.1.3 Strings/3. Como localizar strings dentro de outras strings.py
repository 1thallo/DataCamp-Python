"""
Como localizar strings dentro de outras strings

Muitas vezes, quando estamos trabalhando com strings, nos preocupamos com os caracteres que estão na string. 
Por exemplo, talvez você queira saber quantos cookies em uma lista de cookies têm a palavra Chocolate ou quantos começam com a letra C. 
Você pode realizar essas verificações usando a palavra-chave in e o método .startswith() em uma string. 
Também podemos usar condicionais em uma compreensão de lista na forma de [action for item in list if something is true]. 
Usando nossos exemplos de cookies, seria algo como [cookie_name for cookie_name in cookies if 'chocolate' in cookie_name.lower()]. 
Observe que essas verificações diferenciam maiúsculas de minúsculas, portanto, estamos usando o método .lower() na string. 
Também podemos "encadear" métodos, chamando-os um após o outro.
"""

# --- Código abaixo ---

# Store a list of girl_names that start with s: names_with_s
names_with_s = [name for name in girl_names if name.lower().startswith('s')]

print(names_with_s)

# Store a list of girl_names that contain angel: names_with_angel
names_with_angel = [name for name in girl_names if 'angel' in name.lower()]

print(names_with_angel)