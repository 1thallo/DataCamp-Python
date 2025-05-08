"""
Instruções 1/3

Imprima o atributo salary de emp.
Os atributos não são somente leitura: use a atribuição (sinal de igualdade) para aumentar o atributo salary de emp em 1500 e imprima-o novamente.
"""

# -- Código para Instrução 1 --

class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary 

# Criando o objeto emp e definindo nome e salário
emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

# Imprimir o salário atual do emp
print(emp.salary)

# Aumentar o salário diretamente usando atribuição
emp.salary += 1500

# Imprimir o salário novamente
print(emp.salary)


"""
Instruções 2/3

Aumentar o salário de um funcionário é um padrão comum de comportamento, portanto, deve fazer parte da definição da classe.
Adicione um método give_raise() a Employee que aumente o salário pelo valor passado para give_raise() como parâmetro.
"""

# -- Código para Instrução 2 --

class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary 

    # Adicionando o método give_raise()
    def give_raise(self, value):
        self.salary += value


# Criando o objeto emp e definindo nome e salário
emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

# Imprimir o salário atual do emp
print(emp.salary)

# Usar give_raise() para dar um aumento
emp.give_raise(1500)

# Imprimir o salário após o aumento
print(emp.salary)


"""
Instruções 3/3

Os métodos não precisam apenas modificar os atributos, eles também podem retornar valores!
Adicione um método monthly_salary() cujo return seja o valor do atributo .salary dividido por 12.
Chame .monthly_salary() em emp, atribua-o a mon_sal e imprima.
"""

# -- Código para Instrução 3 --

class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary 

    def give_raise(self, amount):
        self.salary += amount

    # Método monthly_salary para calcular o salário mensal
    def monthly_salary(self):
        return self.salary / 12

# Criando o objeto emp e definindo nome e salário
emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

# Calcular e imprimir o salário mensal
mon_sal = emp.monthly_salary()

# Imprimir o salário mensal
print(mon_sal)
