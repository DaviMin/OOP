# task  - implent a Class human.
# Class fields should store the following_ full name, date of birth, contact, number, city, counrey, home adress.
# implement class methods for dtaa input and output, provide access to individual fields thtough class methods.

class Human:
    def __init__(self, name, date_of_birth, contact, city, country, home_address):
        self.name = name
        self.date_of_birth = date_of_birth
        self.contact = contact
        self.city = city
        self.country = country
        self.home_address = name

    def get_name(self):
        return self.__name # __ na zacatku znamena, ze to jsou privatni data jen pro danou funkci
        # zvnejsku se do toho uz nemuzu dostat
    def set_name(self, new_name):
        if len(new_name) < 3:
            return False
        self.__name = new_name
        return True

h1 = Human("Human1", "birth1", "contact1", "city1", "country1", "address1")
h2 = Human("Human2", "birth2", "contact2", "city2", "country2", "address2")

print(h1.get_name()) # tady s eobchazi to volani privatni aktivity
#h1.__name == "Nove jmeno" # tohle by neproslo
h1.set_name("Nove jmeno")
print(h1.get_name())