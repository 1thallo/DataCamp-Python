"""
Crie sua primeira classe

É hora de escrever sua primeira classe! Neste exercício, você começará a criar a classe Employee que explorou brevemente na lição anterior. 
Você começará criando métodos que definem atributos e, em seguida, adicionará alguns métodos que os manipulam.

Conforme mencionado no primeiro vídeo, uma abordagem orientada a objetos é mais útil quando seu código envolve interações complexas de muitos objetos. 
No código de produção real, as classes podem ter dezenas de atributos e métodos com lógica complicada, mas a estrutura subjacente é a mesma da classe mais simples.

Suas classes neste curso terão apenas alguns atributos e métodos curtos, mas os princípios organizacionais por trás delas serão diretamente traduzíveis em códigos mais complicados.

Instruções:
- Crie uma classe vazia chamada Employee.
- Crie um objeto emp dessa classe e tente acessar o atributo .name (isso deve causar erro, pois ainda não foi definido).
- Adicione um método set_name(self, new_name) à classe para definir o atributo .name.
- Use set_name() para atribuir o nome 'Korel Rossi' ao emp.
- Adicione um método set_salary(self, new_salary) para definir o atributo .salary.
- Use set_salary() para definir o salário de emp como 50000.
- Imprima emp.salary após a definição.
"""

# -- Código --

# Define the Employee class
class Employee:
    
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary

# Create an object emp of class Employee
emp = Employee()

# Set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')

# Set the salary of emp to 50000
emp.set_salary(50000)

# Print the salary of emp
print(emp.salary)

# Optional: Check available attributes/methods
# print(dir(emp))
