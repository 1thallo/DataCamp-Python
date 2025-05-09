"""
Instrução 1/4:
Crie uma classe Customer com o método __init__() que:
- Recebe os parâmetros name e new_bal,
- Atribui name ao atributo name,
- Levanta um ValueError se new_bal for negativo,
- Caso contrário, atribui new_bal ao atributo _balance (com _).
"""

# Create a Customer class
class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
            raise ValueError("Erro de valor!")
        self._balance = new_bal

"""
Instrução 2/4:
Adicione um método balance() com um decorador @property que retorna o atributo _balance.
"""

class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal  
    
    # Add a decorated balance() method returning _balance
    @property
    def balance(self):
        return self._balance


"""
Instrução 3/4:
Defina outro método balance() para servir como setter, com o decorador apropriado e um parâmetro adicional:
- Levante um ValueError se o parâmetro for negativo,
- Caso contrário, atribua-o a _balance;
- Imprima "Setter method is called".
"""

class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal  

    # Add a decorated balance() method returning _balance        
    @property
    def balance(self):
        return self._balance
     
    # Add a setter balance() method
    @balance.setter
    def balance(self, new_bal):
        # Validate the parameter value
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal
        
        # Print "Setter method is called"
        print("Setter method is called")


"""
Instrução 4/4:
- Crie um Customer chamado Belinda Lutz com o saldo de 2000 e salve-o como cust.
- Use a sintaxe de ponto e = para atribuir 3000 a cust.balance.
- Imprima cust.balance.
"""

class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal  

    # Add a decorated balance() method returning _balance        
    @property
    def balance(self):
        return self._balance

    # Add a setter balance() method
    @balance.setter
    def balance(self, new_bal):
        # Validate the parameter value
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal
        print("Setter method called")

# Create a Customer        
cust = Customer("Belinda Lutz", 2000)

# Assign 3000 to the balance property
cust.balance = 3000

# Print the balance property
print(cust.balance)