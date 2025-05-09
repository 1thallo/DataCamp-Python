# Ao comparar dois objetos de uma classe personalizada usando ==, o Python, por padrão,
# compara apenas as referências de objeto, não os dados contidos nos objetos.
# Para substituir esse comportamento, a classe pode implementar o método especial __eq__(),
# que aceita dois argumentos – os objetos a serem comparados – e retorna True ou False.
# Esse método será chamado implicitamente quando dois objetos forem comparados.

# A classe BankAccount do capítulo anterior está disponível para você no painel de script.
# Ela tem um atributo, balance, e um método withdraw().
# Duas contas bancárias com o mesmo saldo não são necessariamente a mesma conta,
# mas uma conta bancária geralmente tem um número de conta,
# e duas contas com o mesmo número de conta devem ser consideradas a mesma.

# Instruções:
# - Modifique o método __init__() para aceitar um novo parâmetro number,
#   e inicialize um novo atributo number.
# - Defina um método __eq__() que retorne True se o atributo number de dois objetos for igual.
# - Examine as instruções de impressão e a saída no console.

class BankAccount:
    # MODIFY to initialize a number attribute
    def __init__(self, number, balance=0):
        self.balance = balance
        self.number = number

    def withdraw(self, amount):
        self.balance -= amount 
    
    # Define __eq__ that returns True if the number attributes are equal 
    def __eq__(self, other):
        return self.number == other.number   

# Create accounts and compare them       
acct1 = BankAccount(123, 1000)
acct2 = BankAccount(123, 1000)
acct3 = BankAccount(456, 1000)

print(acct1 == acct2)  # True, same account number
print(acct1 == acct3)  # False, different account number
