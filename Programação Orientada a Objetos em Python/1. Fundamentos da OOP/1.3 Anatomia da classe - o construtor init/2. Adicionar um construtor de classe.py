"""
Instruções 1/3

Defina a classe Employee com um construtor __init__() que:

aceite dois argumentos, name e salary (com valor padrão 0),

crie dois atributos, também chamados de name e salary,

defina seus valores para os argumentos correspondentes.
"""

# -- Código para Instrução 1 --

class Employee:
    # Create __init__() method
    def __init__(self, name, salary=0):
        # Create the name and salary attributes
        self.name = name
        self.salary = salary
    
    # From the previous lesson
    def give_raise(self, amount):
        self.salary += amount

    def monthly_salary(self):
        return self.salary/12
        
emp = Employee("Korel Rossi")
print(emp.name)
print(emp.salary)


"""
Instruções 2/3

O método __init__() é um ótimo lugar para fazer o pré-processamento.

Modifique __init__() para verificar se o parâmetro salary é positivo:
Se sim, atribua-o ao atributo salary,
Caso contrário, atribua 0 ao atributo e imprima "Invalid salary!".
"""

# -- Código para Instrução 2 --

class Employee:
  
    def __init__(self, name, salary=0):
        self.name = name
        # Modify code below to check if salary is positive
        if salary >= 0:
            self.salary = salary
        else:
            self.salary = 0
            print("Invalid salary!") 

    def give_raise(self, amount):
        self.salary += amount

    def monthly_salary(self):
        return self.salary/12
        
emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)


"""
Instruções 3/3

Importe datetime do módulo datetime. Isso contém a função que retorna a data atual.

Adicione um atributo hire_date e defina-o como datetime.today().
"""

# -- Código para Instrução 3 --

# Import datetime from datetime
from datetime import datetime

class Employee:
    
    def __init__(self, name, salary=0):
        self.name = name
        if salary > 0:
            self.salary = salary
        else:
            self.salary = 0
            print("Invalid salary!")
        
        # Add the hire_date attribute and set it to today's date
        self.hire_date = datetime.today()

    def give_raise(self, amount):
        self.salary += amount

    def monthly_salary(self):
        return self.salary/12
        
emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)
print(emp.hire_date)
