"""
Usando classes de dados

Vamos colocar em uso a classe de dados WeightEntry que criamos no exercício anterior. 
Criaremos uma instância de WeightEntry para cada entrada no weight_log e, em seguida, usaremos a propriedade mass_to_flipper_length_ratio 
que adicionamos para realizar o cálculo. 

Aqui está um lembrete da nossa classe de dados WeightEntry:

@dataclass
class WeightEntry:
    # Define the fields on the class
    species: str
    flipper_length: int
    body_mass: int
    sex: str

    @property
    def mass_to_flipper_length_ratio(self):
        return self.body_mass / self.flipper_length

Instruções:
- Crie uma lista vazia chamada labeled_entries.
- Itere entre as entradas de weight_log usando a expansão de tuplas para separar species, flipper_length, body_mass, sex.
- Acrescente uma nova instância da classe de dados WeightEntry para cada entrada em labeled_entries.
- Imprima uma lista dos primeiros 5 valores de mass_to_flipper_length_ratio usando uma compreensão de lista.
"""

# -- Código --

# Create the empty list: labeled_entries
labeled_entries = []

# Iterate over the weight_log entries
for species, flipper_length, body_mass, sex in weight_log:
    # Append a new WeightEntry instance to labeled_entries
    labeled_entries.append(WeightEntry(species, flipper_length, body_mass, sex))

# Print a list of the first 5 mass_to_flipper_length_ratio values
print([entry.mass_to_flipper_length_ratio for entry in labeled_entries[:5]])
