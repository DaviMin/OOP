from animal import Animal
from walkable import Walkable
from flyable import Flyable

class Parrot(Animal, Walkable, Flyable):
    def walk(self):
        print("parrot walking")

    def fly(self):
        print("parrot flying")

# Tady se demonstruje co vsechno se da pro chicken a prrot dedit a neco pridat - daji se dedit rozne class