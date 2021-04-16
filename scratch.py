from datetime import date

class Animal:
    def __init__(self, name, species, food, chip_number):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.food = food,
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

danny = Llama("Danny", "Alpaca", "Shift B", "Llama food", 12345)

print(danny.chip_number)