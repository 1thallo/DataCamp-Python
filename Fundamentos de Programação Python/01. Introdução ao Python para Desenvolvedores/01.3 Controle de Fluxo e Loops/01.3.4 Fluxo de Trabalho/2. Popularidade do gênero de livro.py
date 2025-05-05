# Popularidade do Gênero de Livro

# Enunciado:
# Anteriormente, você trabalhou com um dicionário que contém informações sobre autores e o número de livros que eles escreveram.
# Neste exercício, os dados sobre os mesmos autores foram agregados para criar um novo dicionário chamado `genre_sales`,
# em que as chaves são o gênero e os valores são as vendas médias desse gênero entre os 20 autores mais populares.
#
# Seu trabalho é encontrar os gêneros mais e menos populares entre esses autores, juntamente com a receita média de vendas deles.

# ## Instruções:
# 1. Verifique se `average_sale` é igual à maior receita de vendas (5166000000) em `genre_sales`.
# 2. Imprima o `genre` com a maior média de vendas.
# 3. Em seguida, verifique se `average_sale` é igual à menor receita de vendas (80000000).
# 4. Por fim, imprima o `genre` com a menor média de vendas.

# --- Código abaixo ---

# Filter for the maximum sales value
if average_sale == 5166000000:
  
  # Print the genre
  print("Most popular genre: ", genre)
  print("Average sales: ", average_sale)

# Filter for the minimum sales value
elif average_sale == 80000000:
  
  # Print the genre
  print("Least popular genre: ", genre)
  print("Average sales: ", average_sale)