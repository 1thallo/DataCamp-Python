"""
Instruções 1/2

Adicione um método de classe from_str() que:
- aceite uma string datestr no formato 'YYYY-MM-DD',
- divida datestr e converta cada parte em um número inteiro,
- retorne uma instância da classe com os atributos definidos para os valores extraídos de datestr.
"""

# -- Código --

class BetterDate:    
    # Constructor
    def __init__(self, year, month, day):
        # Recall that Python allows multiple variable assignments in one line
        self.year, self.month, self.day = year, month, day
    
    # Define a class method from_str
    @classmethod
    def from_str(cls, datestr):
        # Split the string at "-" and convert each part to integer
        parts = datestr.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        # Return the class instance
        return cls(year, month, day)
        
bd = BetterDate.from_str('2020-04-30')   
print(bd.year)
print(bd.month)
print(bd.day)

"""
Instruções 2/2

Adicione um método de classe from_datetime() que:
- aceite um objeto datetime como argumento,
- use seus atributos .year, .month e .day para criar um objeto BetterDate com os mesmos valores de atributo.
"""

# -- Código --

# import datetime from datetime
from datetime import datetime

class BetterDate:
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)

    # Define a class method from_datetime accepting a datetime object
    @classmethod
    def from_datetime(cls, dateobj):
        year, month, day = dateobj.year, dateobj.month, dateobj.day
        return cls(year, month, day)

# You should be able to run the code below with no errors: 
today = datetime.today()     
bd = BetterDate.from_datetime(today)   
print(bd.year)
print(bd.month)
print(bd.day)
