"""
Uso de atributos internos
Neste exercício, você voltará à classe BetterDate do Capítulo 2.

Você decide adicionar um método que verifica a validade da data, mas não quer torná-lo parte da interface pública de BetterDate.

A classe BetterDate está disponível no painel de script.

Instruções:
- Adicione um atributo de classe _MAX_DAYS que armazena o número máximo de dias em um mês: 31.
- Adicione outro atributo de classe que armazene o número máximo de meses em um ano: 12. Use a convenção de nomenclatura apropriada para indicar que esse é um atributo interno.
- Adicione um método _is_valid() que retorne True se os atributos day e month forem menores ou iguais aos valores máximos correspondentes e False caso contrário. Certifique-se de se referir aos atributos da classe por seus nomes!
"""

# Início do código
# Add class attributes for max number of days and months
class BetterDate:
    _MAX_DAYS = 31
    _MAX_MONTH = 12
    
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day
        
    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)
    
    # Add _is_valid() checking day and month values
    def _is_valid(self):
        if self.day <= BetterDate._MAX_DAYS and self.month <= BetterDate._MAX_MONTH:
            return True
        else:
            return False
    
bd1 = BetterDate(2020, 4, 30)
print(bd1._is_valid())

bd2 = BetterDate(2020, 6, 45)
print(bd2._is_valid())