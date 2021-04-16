from models.attractions import PettingZoo
from models import (Llama,
                    PettingZoo,
                    Lemur)

danny = Llama("Danny", "Alpaca", "Shift B", "Llama food")
zoo = PettingZoo("Big Zoo", "A place for fuzzies")
zoo.admit(danny)

zoo.roster()
