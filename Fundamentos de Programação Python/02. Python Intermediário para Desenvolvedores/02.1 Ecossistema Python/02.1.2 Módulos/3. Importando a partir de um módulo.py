# Importando a partir de um Módulo

# Enunciado:
# Outro módulo útil é o `datetime`, que permite que você crie e trabalhe com datas e horas,
# bem como fusos horários e períodos de tempo!
#
# O módulo `datetime` tem uma função chamada `date`.
#
# Neste exercício, você praticará a importação e o uso do método `date` do módulo `datetime` e o usará para criar uma variável.

# ## Instruções:
# 1. Importe a função `date` do módulo `datetime`.
# 2. Crie uma variável chamada `deadline`, atribuindo uma chamada de `date()`, passando os números 2024, 1 e 19, nessa ordem, separados por vírgulas.
# 3. Verifique o tipo de dado de `deadline`.
# 4. Imprima a variável `deadline`.

# --- Código abaixo ---

from datetime import date
deadline = date(2024, 1, 19)

print(type(deadline))
print(deadline)