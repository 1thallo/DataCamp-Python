# Usando * e zip para 'descompactar'

# Você sabe como usar zip() e também como imprimir valores de um objeto zip. Excelente!
#
# Vamos brincar um pouco mais com zip(). Não há função de descompactação para fazer o inverso do que o zip() faz. 
# No entanto, você pode reverter o que foi compactado usando zip() com uma pequena ajuda de *! 
# * descompacta um iterável, como uma lista ou uma tupla, em argumentos posicionais em uma chamada de função.
#
# Neste exercício, você usará * em uma chamada de zip() para desempacotar as tuplas produzidas por zip().
#
# Duas tuplas de strings, mutants e powers, foram pré-carregadas.

# Instruções:
# 1. Crie um objeto zip usando zip() em mutants e powers, nessa ordem. Atribua o resultado a z1.
# 2. Imprima as tuplas em z1 descompactando-as em argumentos posicionais usando o operador * em uma chamada print().
# 3. Como a chamada anterior para print() teria esgotado os elementos em z1, recrie o objeto zip que você definiu anteriormente e atribua o resultado novamente a z1.
# 4. "Descompacte" as tuplas em z1, descompactando-as em argumentos posicionais usando o operador * em uma chamada zip(). 
#    Atribua os resultados a result1 e result2, nessa ordem.
# 5. Os últimos comandos print() imprimem a saída da comparação de result1 com mutants e result2 com powers. 
#    Clique em Submit Answer para ver se os arquivos descompactados result1 e result2 são equivalentes a mutants e powers, respectivamente.

# --- Código abaixo ---

# Create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# Print the tuples in z1 by unpacking with *
print(*z1)

# Re-create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = zip(*z1)

# Check if unpacked tuples are equivalent to original tuples
print(result1 == mutants)
print(result2 == powers)