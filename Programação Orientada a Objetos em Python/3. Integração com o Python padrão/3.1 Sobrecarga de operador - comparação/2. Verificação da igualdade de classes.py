# Verificação da igualdade de classes
# No exercício anterior, você definiu uma classe BankAccount com um atributo number que foi usado para comparação.
# Mas se você comparar um objeto BankAccount com um objeto de outra classe que também tenha um atributo number, poderá obter resultados inesperados.
#
# Por exemplo, considere duas classes:
#
# class Phone:
#   def __init__(self, number):
#      self.number = number
#
#   def __eq__(self, other):
#     return self.number == other.number
#
# pn = Phone(873555333)
#
# class BankAccount:
#   def __init__(self, number):
#      self.number = number
#
#   def __eq__(self, other):
#     return self.number == other.number
#
# acct = BankAccount(873555333)
#
# A execução de acct == pn retornará True, mesmo que estejamos comparando um número de telefone com um número de conta bancária.
# É uma boa prática verificar a classe dos objetos passados para o método __eq__() para garantir que a comparação faça sentido.
#
# Instruções:
# Both the Phone and the BankAccount classes have been defined.
# Try running the code as-is using the "Run code" button and examine the output.
# Modifique a definição de BankAccount para apenas retornar True se o atributo number for o mesmo
# e o type() de ambos os objetos passados para ele for o mesmo.
# Execute o código e examine a saída novamente.

class BankAccount:
    def __init__(self, number, balance=0):
        self.number, self.balance = number, balance
      
    def withdraw(self, amount):
        self.balance -= amount 

    # MODIFY to add a check for the type()
    def __eq__(self, other):
        return (self.number == other.number) and (type(self) == type(other))

acct = BankAccount(873555333)
pn = Phone(873555333)
print(acct == pn)
