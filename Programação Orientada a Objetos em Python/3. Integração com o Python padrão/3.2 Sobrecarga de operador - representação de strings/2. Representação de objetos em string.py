"""
Representação de objetos em string
Existem dois métodos especiais em Python que retornam uma representação de string de um objeto. __str__() é chamado quando você usa print() ou str() em um objeto, e __repr__() é chamado quando você usa repr() em um objeto, imprime o objeto no console sem chamar print(), ou em vez de __str__() se __str__() não estiver definido.

__str__() deve fornecer uma saída "amigável" que descreva um objeto, e __repr__() deve retornar a expressão que, quando avaliada, retornará o mesmo objeto, garantindo a reprodutibilidade do seu código.

Neste exercício, você continuará a trabalhar com a classe Employee do Capítulo 2.

Instruções 1/2
Adicione o método __str__() à classe Employee que retorna uma string contendo o nome e o salário do funcionário. O método deve retornar uma string no seguinte formato:

Employee name: Amar Howard
Employee salary: 40000
"""

# resposta instrucao 1:
class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary
            
    # Add the __str__() method
    def __str__(self):
        return "Employee name: {name}\nEmployee salary: {salary}".format(name=self.name, salary=self.salary)

emp1 = Employee("Amar Howard", 30000)
print(emp1)
emp2 = Employee("Carolyn Ramirez", 35000)
print(emp2)

"""
Instruções 2/2
Adicione o método __repr__() à classe Employee que retorna uma string contendo o nome e o salário do funcionário. O método deve retornar uma string no seguinte formato:

Employee("Amar Howard", 40000)
"""

# resposta instrucao 2:
class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary
      

    def __str__(self):
        s = "Employee name: {name}\nEmployee salary: {salary}".format(name=self.name, salary=self.salary)      
        return s
      
    # Add the __repr__method  
    def __repr__(self):
        return "Employee(\"{name}\", {salary})".format(name=self.name, salary=self.salary)
        
emp1 = Employee("Amar Howard", 30000)
print(repr(emp1))
emp2 = Employee("Carolyn Ramirez", 35000)
print(repr(emp2))
