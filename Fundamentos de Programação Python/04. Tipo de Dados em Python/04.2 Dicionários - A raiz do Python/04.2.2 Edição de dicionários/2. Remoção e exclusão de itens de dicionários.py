"""
Remoção e exclusão de itens de dicionários

Muitas vezes, você vai querer remover chaves e valores de um dicionário. Você pode fazer isso usando a instrução del do Python. 
É importante lembrar que del vai gerar um KeyError se a chave que você estiver tentando excluir não existir. 
Você não pode usá-lo com o método .get() para excluir itens; no entanto, ele pode ser usado com try: catch:.

Se você quiser salvar esses dados excluídos em outra variável para processamento posterior, o método de dicionário .pop() fará exatamente isso. 
Você pode fornecer um valor padrão para .pop() da mesma forma que fez para .get() para lidar com chaves faltantes. 
Também é comum usar .pop() em vez de del, pois esse é um método seguro.
"""

# --- Código abaixo ---

# Remove "Madison Square Park" from squirrels_by_park
squirrels_madison = squirrels_by_park.pop("Madison Square Park")

# Safely remove "City Hall Park" from squirrels_by_park with an empty dictionary as the default
squirrels_city_hall = squirrels_by_park.pop("City Hall Park", {})

# Delete "Union Square Park" from squirrels_by_park
del squirrels_by_park["Union Square Park"]

# Print squirrels_by_park
print(squirrels_by_park)