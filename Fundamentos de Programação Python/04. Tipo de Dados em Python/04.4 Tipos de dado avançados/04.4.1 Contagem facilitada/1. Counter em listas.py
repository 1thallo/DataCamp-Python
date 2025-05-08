"""
Uso do Counter em listas

Counter é uma ferramenta poderosa para contar, validar e aprender mais sobre os elementos em um conjunto de dados que se encontra no módulo collections. 
Você passa um iterável (lista, conjunto, tupla) ou um dicionário para o Counter. 
Você também pode usar o objeto Counter de forma semelhante a um dicionário com atribuição de chave/valor, por exemplo, counter[key] = value.

Um uso comum de Counter é verificar a consistência dos dados antes de usá-los, portanto, vamos fazer exatamente isso.
"""

# --- Código abaixo ---

# Import the Counter object 
from collections import Counter

# Create a Counter of the penguins sex using a list comp
penguins_sex_counts = Counter([penguin['Sex'] for penguin in penguins])

# Print the penguins_sex_counts
print(penguins_sex_counts)