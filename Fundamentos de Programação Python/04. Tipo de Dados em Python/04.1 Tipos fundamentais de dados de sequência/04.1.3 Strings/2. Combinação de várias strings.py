"""
Combinação de várias strings

As f-strings funcionam muito bem para algumas variáveis, mas e se você quiser combinar uma lista inteira de variáveis em uma string? 
Você pode usar o método "".join() exatamente para isso. Você coloca o que deseja unir aos itens da lista dentro de "" e, 
em seguida, passa a lista para o método join(). Por exemplo, se você quiser juntar todos os itens de uma lista denominada cookies 
com uma vírgula e um espaço, ela ficará assim: ", ".join(cookies).

Neste exercício, você usará essas habilidades para converter uma lista dos dez principais nomes de meninos em uma frase armazenada em uma string.
"""

# --- Código abaixo ---

# The top ten boy names are: as preamble
preamble = "The top ten boy names are: "

# , and as conjunction
conjunction = ", and"

# Combines the first 9 names in boy_names with a comma and space as first_nine_names
first_nine_names = ", ".join(boy_names[0:9])

# Print f-string preamble, first_nine_names, conjunction, the final item in boy_names and a period
print(f"{preamble}{first_nine_names}{conjunction} {boy_names[-1]}.")