"""
Instruções 1/2

Importe pandas como pd.
Defina a classe LoggedDF herdada de pd.DataFrame.
Defina um construtor com argumentos *args e **kwargs que:
- chama o construtor pd.DataFrame com os mesmos argumentos,
- atribui datetime.today() a self.created_at.
"""

# -- Código --

# Import pandas as pd
import pandas as pd
from datetime import datetime

# Define LoggedDF inherited from pd.DataFrame and add the constructor
class LoggedDF(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        pd.DataFrame.__init__(*args, **kwargs)
        self.created_at = datetime.today()
    
ldf = LoggedDF({"col1": [1,2], "col2": [3,4]})
print(ldf.values)
print(ldf.created_at)


"""
Instruções 2/2

Adicione um método to_csv() para LoggedDF que:
- copia self para um DataFrame temporário usando .copy(),
- cria uma nova coluna created_at no DataFrame temporário e a preenche com self.created_at,
- chama pd.DataFrame.to_csv() na variável temporária.
"""

# -- Código --

# Import pandas as pd
import pandas as pd
from datetime import datetime

# Define LoggedDF inherited from pd.DataFrame and add the constructor
class LoggedDF(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        pd.DataFrame.__init__(self, *args, **kwargs)
        self.created_at = datetime.today()
    
    def to_csv(self, *args, **kwargs):
        # Copy self to a temporary DataFrame
        temp = self.copy()
        
        # Create a new column filled with self.created_at
        temp["created_at"] = self.created_at
        
        # Call pd.DataFrame.to_csv on temp, passing in *args and **kwargs
        pd.DataFrame.to_csv(temp, *args, **kwargs)
