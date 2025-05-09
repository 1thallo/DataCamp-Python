"""
Instrução 1/3:
- Atribua um novo valor de '2035-07-13' ao atributo created_at.
- Imprima o valor do atributo created_at de ldf para verificar se sua atribuição foi bem-sucedida.
"""

import pandas as pd
from datetime import datetime

# LoggedDF class definition from Chapter 2
class LoggedDF(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        pd.DataFrame.__init__(self, *args, **kwargs)
        self.created_at = datetime.today()

    def to_csv(self, *args, **kwargs):
        temp = self.copy()
        temp["created_at"] = self.created_at
        pd.DataFrame.to_csv(temp, *args, **kwargs)   

# Instantiate a LoggedDF called ldf
ldf = LoggedDF({"col1": [1,2], "col2":[3,4]}) 

# Assign a new value to ldf's created_at attribute and print
ldf.created_at = '2035-07-13'
print(ldf.created_at)

"""
Instrução 2/3:
- Crie um atributo interno chamado _created_at para transformar created_at em um atributo somente leitura.
- Modifique a classe para usar o atributo interno, _created_at, no lugar de created_at.
"""

import pandas as pd
from datetime import datetime

# MODIFY the class to use _created_at instead of created_at
class LoggedDF(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        pd.DataFrame.__init__(self, *args, **kwargs)
        self._created_at = datetime.today()
    
    def to_csv(self, *args, **kwargs):
        temp = self.copy()
        temp["created_at"] = self._created_at
        pd.DataFrame.to_csv(temp, *args, **kwargs)   
    
    # Add a read-only property: _created_at
    @property  
    def created_at(self):
        return self._created_at

# Instantiate a LoggedDF called ldf
ldf = LoggedDF({"col1": [1,2], "col2":[3,4]}) 

"""
Instrução 3/3:
- Pergunta: O que acontece quando você atribui '2035-07-13' a ldf.created_at?
Resposta Certa: Um AttributeError é lançado, pois ldf.created_at é somente leitura.
"""

# Attempting to assign a new value to ldf.created_at
try:
    ldf.created_at = '2035-07-13'
except AttributeError as e:
    print(e)