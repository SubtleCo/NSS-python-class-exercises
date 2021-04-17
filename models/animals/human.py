from . import Animal
from models.movements import Walking, Swimming

class Human(Animal, Walking, Swimming):
    def __init__(self, name, species, shift, food, chip_number):
        Animal.__init__(self, name, species, food, chip_number)
        Walking.__init__(self)
        Swimming.__init__(self)
        self.shift = shift

    def talk(self):
        print(f"{self.name} is all 'blah, blah")
    
    def run(self):
        print(f"{self.name} fuckin books it")