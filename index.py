from models.attractions import PettingZoo
from models import (Llama,
                    PettingZoo,
                    Lemur)

danny = Llama("Danny", "Alpaca", "Shift B", "Llama food", 12345)
zoo = PettingZoo("Big Zoo", "A place for fuzzies")
zoo.admit(danny)

zoo.roster()

print(danny.chip_number)
danny.chip_number = 54321
print(danny.chip_number)
print(zoo.last_critter_added)