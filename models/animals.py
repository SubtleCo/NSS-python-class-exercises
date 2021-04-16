from datetime import date

class Animal:
    def __init__(self, name, species, food, chip_number):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.food = food
        self.__chip_number = chip_number

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    @property # the getter
    def chip_number(self):
        return self.__chip_number

    @chip_number.setter # the (fake) setter
    def chip_number(self, fake_value):
        pass

class Llama(Animal):
    def __init__(self, name, species, shift, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.shift = shift,
        self.walking = True

class Goat(Animal):
    def __init__(self, name, species, shift, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.shift = shift,
        self.walking = True

class Tiger(Animal):
    def __init__(self, name, species, shift, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.shift = shift,
        self.walking = True

class Lemur(Animal):
    def __init__(self, name, species, shift, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.shift = shift,
        self.walking = True

class Human(Animal):
    def __init__(self, name, species, shift, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.shift = shift,
        self.walking = True

class Cobra(Animal):
    def __init__(self, name, species, shift, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.shift = shift,
        self.slithering = True
        
class Cottonmouth(Animal):
    def __init__(self, name, species, shift, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.shift = shift,
        self.slithering = True

class Rattlesnake(Animal):
    def __init__(self, name, species, shift, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.shift = shift,
        self.slithering = True
        
class Garter_Snake(Animal):
    def __init__(self, name, species, shift, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.shift = shift,
        self.slithering = True
        
class Slimy(Animal):
    def __init__(self, name, species, shift, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.shift = shift,
        self.slithering = True
        
class Clownfish(Animal):
    def __init__(self, name, species, shift, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.shift = shift,
        self.swimming = True
        
class Marlin(Animal):
    def __init__(self, name, species, shift, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.shift = shift,
        self.swimming = True
        
class Dolphin(Animal):
    def __init__(self, name, species, shift, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.shift = shift,
        self.swimming = True
        
class Whale(Animal):
    def __init__(self, name, species, shift, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.shift = shift,
        self.swimming = True
        
class Turtle(Animal):
    def __init__(self, name, species, shift, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.shift = shift,
        self.swimming = True