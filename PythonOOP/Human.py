# task  - implent a Class human.
# Class fields should store the following_ full name, date of birth, contact, number, city, counrey, home adress.
# implement class methods for dtaa input and output, provide access to individual fields thtough class methods.

class Human:
    def __init__(self, name):
        self.name = name


    def start(self):
        print(f"brmbrm startuju vozidlo {self.name}")