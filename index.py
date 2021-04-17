from models import (Llama,
                    Petting_Zoo,
                    Human,
                    Garter_Snake)

danny = Llama("Danny", "Alpaca", "Shift B", "Llama food", 12345)
zoo = Petting_Zoo("Big Zoo", "A place for fuzzies")
alex = Human("Alex", "Regular Human", "Shift A", "Waffles", 666)
zoo.admit(danny)
zoo.admit(alex)
ekans = Garter_Snake("Ekans", "CrazySnake", "Shift B", "mice", 32323)
zoo.admit(ekans)
zoo.roster()



