# Usando zip

# Outra função interessante que você aprendeu é zip(), que recebe qualquer número de iteráveis e retorna um objeto zip que é um iterador de tuplas. 
# Se você quiser imprimir os valores de um objeto zip, poderá convertê-lo em uma lista e depois imprimi-lo. 
# Imprimir apenas um objeto zip não retornará os valores, a menos que você o descompacte primeiro. 
# Neste exercício, você explorará isso por si mesmo.

# Três listas de strings são pré-carregadas: mutants, aliases e powers. 
# Primeiro, você usará list() e zip() nessas listas para gerar uma lista de tuplas. 
# Em seguida, você criará um objeto zip usando zip(). 
# Por fim, você desempacotará esse objeto zip em um loop for para imprimir os valores em cada tupla. 
# Observe a saída diferente gerada pela impressão da lista de tuplas, depois o objeto zip e, por fim, os valores das tuplas no loop for.

# Instruções:
# 1. Usando zip() com list(), crie uma lista de tuplas a partir das três listas mutants, aliases e powers (nessa ordem) e atribua o resultado a mutant_data.
# 2. Usando zip(), crie um objeto zip chamado mutant_zip a partir das três listas mutants, aliases e powers.
# 3. Conclua o loop for desempacotando o objeto zip que você criou e imprimindo os valores da tupla. 
#    Use value1, value2, value3 para os valores de cada um de mutants, aliases e powers, nessa ordem.

# --- Código abaixo ---

# Create a list of tuples: mutant_data
mutant_data = list(zip(mutants, aliases, powers))

# Print the list of tuples
print(mutant_data)

# Create a zip object using the three lists: mutant_zip
mutant_zip = zip(mutants, aliases, powers)

# Print the zip object
print(mutant_zip)

# Unpack the zip object and print the tuple values
for value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)