from animal import Animal
from walkable import Walkable

class Chicken(Animal, Walkable):
    def walk(self):
        print("chicken kraci")