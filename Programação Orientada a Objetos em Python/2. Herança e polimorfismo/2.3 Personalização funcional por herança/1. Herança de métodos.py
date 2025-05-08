"""
Instruções 1/2

Adicione um construtor para Manager que:
- aceite name, salary (padrão 50000) e project (padrão None);
- chame o construtor da classe Employee com os parâmetros name e salary;
- crie um atributo project e o defina como o parâmetro project.
"""

# -- Código --

class Employee:
    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

class Manager(Employee):
    # Add a constructor 
    def __init__(self, name, salary=50000, project=None):
        # Call the parent's constructor   
        Employee.__init__(self, name, salary)
        # Assign project attribute
        self.project = project

    def display(self):
        print("Manager ", self.name)

"""
Instruções 2/2

Adicione um método give_raise() para Manager que:
- aceite os mesmos parâmetros que Employee.give_raise(), mais um parâmetro bonus com o valor padrão de 1.05;
- multiplique amount por bonus;
- use o método de Employee para aumentar o salário por esse produto.
"""

# -- Código --

class Employee:
    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

class Manager(Employee):
    def display(self):
        print("Manager ", self.name)

    def __init__(self, name, salary=50000, project=None):
        Employee.__init__(self, name, salary)
        self.project = project

    # Add a give_raise method
    def give_raise(self, amount, bonus=1.05):
        return Employee.give_raise(self, amount * bonus)

mngr = Manager("Ashta Dunbar", 78500)
mngr.give_raise(1000)
print(mngr.salary)
mngr.give_raise(2000, bonus=1.03)
print(mngr.salary)
