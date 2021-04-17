from . import Attraction

class Petting_Zoo(Attraction):
    def __init__(self, attraction_name, description):
        super().__init__(attraction_name, description)

    def admit(self, animal):
        try:
            if animal.walk_speed > -1:
                self.animals.append(animal)
                print(f"{animal.name} now lives in {self.attraction_name}")
        except AttributeError as ex:
            print(f"{animal.name} doesn't like to be petted, so pelase do not put it in the {self.attraction_name} attraction.")