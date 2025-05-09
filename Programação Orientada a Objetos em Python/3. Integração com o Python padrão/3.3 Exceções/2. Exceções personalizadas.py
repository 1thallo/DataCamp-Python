"""
Exceções personalizadas

Não é necessário confiar apenas nas exceções incorporadas, como IndexError: 
você pode definir suas próprias exceções mais específicas para o seu aplicativo. 
Você também pode definir hierarquias de exceções. Tudo o que você precisa para 
definir uma exceção é uma classe herdada da classe incorporada Exception ou de 
uma de suas subclasses.

No Capítulo 1, você definiu uma classe Employee e usou as instruções print e os 
valores padrão para lidar com erros como a criação de um funcionário com um 
salário abaixo do mínimo ou a concessão de um aumento muito grande. Uma maneira 
melhor de lidar com essa situação é usar exceções. Como esses erros são 
específicos do nosso aplicativo (ao contrário, por exemplo, de um erro de 
divisão por zero, que é universal), faz sentido usar classes de exceção personalizadas.
"""

"""
Instruções 1/3

Defina uma classe vazia SalaryError herdada da classe ValueError incorporada.
Defina uma classe vazia BonusError herdada da classe SalaryError.
"""
# Defina a classe SalaryError herdando de ValueError
class SalaryError(ValueError):
    pass

# Defina a classe BonusError herdando de SalaryError
class BonusError(SalaryError):
    pass


"""
Instruções 2/3

Complete a definição de __init__() para raise a SalaryError com a mensagem 
"Salary is too low!" se o parâmetro salary for menor que o atributo de classe MIN_SALARY.
Não há necessidade de else porque raise encerra o programa de qualquer forma.
"""
class SalaryError(ValueError): pass
class BonusError(SalaryError): pass

class Employee:
  MIN_SALARY = 30000
  MAX_RAISE = 5000

  def __init__(self, name, salary = 30000):
    self.name = name
    
    # If salary is too low
    if salary > MIN_SALARY:
      # Raise a SalaryError exception
      raise SalaryError("Salary is too low!")
      
    self.salary = salary


"""
Instruções 3/3

Examine o método give_bonus() e reescreva-o usando exceções em vez de 
instruções de impressão:

- levante um BonusError se o valor do bônus for muito alto;
- levante um SalaryError se o resultado da adição do bônus for muito baixo.
"""
class SalaryError(ValueError): pass
class BonusError(SalaryError): pass

class Employee:
  MIN_SALARY = 30000
  MAX_BONUS = 5000

  def __init__(self, name, salary = 30000):
    self.name = name    
    if salary < Employee.MIN_SALARY:
      raise SalaryError("Salary is too low!")      
    self.salary = salary
    
  # Rewrite using exceptions  
  def give_bonus(self, amount):
    if amount > Employee.MAX_BONUS:
      raise BonusError("The bonus amount is too high!")  
        
    elif self.salary + amount <  Employee.MIN_SALARY:
      raise SalaryError("The salary after bonus is too low!")
      
    else:  
      self.salary += amount
