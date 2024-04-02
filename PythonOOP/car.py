# tohle je pro dedicnost (inheritence) Vehicle
# rodic ma nejake vlastnosti a ten dedic ma vzdycky to co rodic a k tomu neco navic - proto Car bere vse co Vehicle


from vehicle import Vehicle

class Car(Vehicle):

    def __init__(self, name, color):
        super().__init__(name)
        # super je odkaz na toho predka - dedit vlastnosti...
        self.color = color

    def turn(selfself, direction):
        print(f"odbocim do {direction}")