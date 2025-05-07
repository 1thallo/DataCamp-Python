"""
Mais do que apenas verdadeiro e falso

O Python tem dois valores booleanos disponíveis para você usar: True e False. 
Mais comumente, esses valores booleanos são usados para indicar que algo está ativo ou inativo, habilitado ou desabilitado, sim ou não, ou estados semelhantes. 
Além disso, muitos tipos do Python retornam valores "verdadeiros" ou "falsos", dependendo de sua condição quando avaliados usando a função bool().
"""

# --- Código abaixo ---

# Create an empty list
my_list = []

# Check the truthiness of my_list
print(bool(my_list))

# Append the string 'cookies' to my_list
my_list.append('cookies')

# Check the truthiness of my_list
print(bool(my_list))