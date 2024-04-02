class City:

    def __init__(self, name, long, lat):
        self.name = name
        self.long = long
        self.lat = lat


    def __str__(self): # nova magic method, kdy se nevola na pamet, kdyz to neni, tak neco chybi v pameti - TODO
        return f"""Name: {self.name}"
Long: {self.long}, Lat: {self.lat}"""


    def __eq__(self, other): # magicmetoda na porovnavani, z potovnavani muze vyjit jenom \true nebo false
        # tady to other znamena jakoze jine mesto
        return self.long == other.long and self.lat == other.lat

c1 = City("Prague", 20, 30)
c2 = City("Berline", 20, 30)
print(c1)
print(c1 == c2) # z toho vyjde porovnani toho EQ - z Prahy a Belrin vbyjde logicky True