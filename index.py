from models import (Llama,
                    Petting_Zoo,
                    Human)

danny = Llama("Danny", "Alpaca", "Shift B", "Llama food", 12345)
zoo = Petting_Zoo("Big Zoo", "A place for fuzzies")
alex = Human("Alex", "Regular Human", "Shift A", "Waffles", 666)
zoo.admit(danny)
zoo.admit(alex)
zoo.roster()



