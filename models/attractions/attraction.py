from datetime import date

class Attraction():
    def __init__(self, attraction_name, description):
        self.attraction_name = attraction_name
        self.description = description
        self.animals = []
        self.date_added = date.today()
        
    def roster(self):
        print('Animals here are')
        for animal in self.animals:
            print(animal.name)

    @property
    def last_critter_added(self):
        return self.animals[-1]