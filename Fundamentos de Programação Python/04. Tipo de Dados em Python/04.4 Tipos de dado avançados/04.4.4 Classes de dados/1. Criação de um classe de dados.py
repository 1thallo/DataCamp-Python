"""
Criação de uma classe de dados

As classes de dados podem oferecer maneiras ainda mais avançadas de armazenar e trabalhar com dados. 
Anteriormente, usamos uma tupla nomeada nas entradas de registro de peso para facilitar o uso de uma estrutura de dados. 
Neste código, usaremos uma classe de dados para fazer a mesma coisa, mas adicionaremos uma property personalizada para retornar 
a relação entre a massa corporal e o comprimento da nadadeira. 

As classes de dados começam com uma coleção de campos e seus tipos. 
Em seguida, você define as propriedades, que são funções na classe de dados que operam sobre ela mesma para retornar informações adicionais sobre os dados. 
Por exemplo, uma classe de dados de pessoa pode ter uma propriedade que calcula a idade atual de alguém com base na data de nascimento e na data atual.

Instruções:
- Importe dataclass de dataclasses.
- Adicione os campos species (string), sex (string), body_mass (int) e flipper_length (int) à classe de dados.
- Adicione uma propriedade (mass_to_flipper_length_ratio) que retorne body_mass dividido por flipper_length.
"""

# -- Código --

# Import dataclass
from dataclasses import dataclass

@dataclass
class WeightEntry:
    # Define the fields on the class
    species: str
    flipper_length: int
    body_mass: int
    sex: str

    # Define a property that returns the body_mass / flipper_length
    @property
    def mass_to_flipper_length_ratio(self):
        return self.body_mass / self.flipper_length
