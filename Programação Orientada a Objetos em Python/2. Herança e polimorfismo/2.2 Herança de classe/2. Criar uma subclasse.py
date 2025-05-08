"""
Instruções 1/2

Adicione uma classe Manager vazia que seja herdada de Employee.
Crie um objeto mng da classe Manager com o nome Debbie Lashko e o salário 86500.
Imprima o nome de mng.
"""

# -- Código --

class Employee:
  MIN_SALARY = 30000    

  def __init__(self, name, salary=MIN_SALARY):
      self.name = name
      if salary >= Employee.MIN_SALARY:
        self.salary = salary
      else:
        self.salary = Employee.MIN_SALARY
        
  def give_raise(self, amount):
      self.salary += amount      
        
# Define a new class Manager inheriting from Employee
class Manager(Employee):
  pass

# Define a Manager object
mng = Manager("Debbie Lashko", 86500)

# Print mng's name
print(mng.name)

"""
Instruções 2/2

Remova a instrução pass e adicione um método display() à classe Manager que imprime apenas a string "Manager" seguida do nome completo.
Chame o método .display() a partir da instância mng.
"""

# -- Código --

class Employee:
  MIN_SALARY = 30000    

  def __init__(self, name, salary=MIN_SALARY):
      self.name = name
      if salary >= Employee.MIN_SALARY:
        self.salary = salary
      else:
        self.salary = Employee.MIN_SALARY
  def give_raise(self, amount):
    self.salary += amount      
        
# MODIFY Manager class and add a display method
class Manager(Employee):
  def display(self):
    print ('Manager')
    print(f'Manager {self.name}')

mng = Manager("Debbie Lashko", 86500)
print(mng.name)

# Call mng.display()
mng.display()
