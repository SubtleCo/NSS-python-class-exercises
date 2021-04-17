from models.animals import Animal

class Goat(Animal):
    def __init__(self, name, species, shift, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.shift = shift,
        self.walking = True