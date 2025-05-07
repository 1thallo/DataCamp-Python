"""
Literais de strings formatadas (f-strings)

Até o momento, temos usado strings simples com "" ou '' nesta aula, mas há vários tipos de strings e variáveis combinadas com elas. 
A adição mais recente de um tipo de string ao Python é a "f-strings", que é a abreviação de literais de string formatadas. 
As "f-strings" facilitam a combinação de strings com variáveis e formatação para ajudar a obter exatamente o resultado que você deseja, 
e você as cria colocando a letra f antes das aspas, como em f"". 
Se quiser colocar uma variável dentro de uma string, pode colocar a variável dentro de {} em uma f-string para inserir o valor da variável na própria string. 
Por exemplo, se tivéssemos uma variável count com o número 12 armazenado, poderíamos criar uma f-string como f"{count} cookies", 
que produziria a string "12 cookies" quando fosse impressa. 
A lista top_ten_girl_names contém tuplas que correspondem a top_ten_rank e name para cada posição.
"""

# --- Código abaixo ---

# Loop over top_ten_girl_names and unpack each tuple into top_ten_rank and name
for top_ten_rank, name in top_ten_girl_names:
    # Print each name in the proper format
    print(f"Rank #: {top_ten_rank} - {name}")