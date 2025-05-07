"""
Impressão de floats

A notação científica é uma ferramenta poderosa para representar números, mas pode ser confusa quando você tenta imprimir valores flutuantes. 
No entanto, podemos usar as f-strings de que falamos antes para garantir que sejam impressas corretamente todas as vezes, usando um especificador de formato. 
Por exemplo, se quisermos formatar uma variável em uma f-string como um float, podemos usar o especificador de formato f, como, por exemplo, print(f"{some_variable:f}"). 
Ele também recebe uma precisão de operação no especificador de formato do float, por exemplo, print(f"{some_variable:.4f}") imprimiria quatro casas decimais de precisão.
"""

# --- Código abaixo ---

# Print floats 1, 2, and 3
print(float1)
print(float2)
print(float3)

# Print floats 2 and 3 using the f string formatter
print(f"{float2:f}")
print(f"{float3:f}")

# Print float 3 with a 7 f string precision
print(f"{float3:.7f}")