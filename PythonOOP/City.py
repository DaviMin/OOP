class City:

    def __init__(self, name, long, lat):
        self.name = name
        self.long = long
        self.lat = lat


    def __str__(self): # nova magic method, kdy se nevola na pamet, kdyz to neni, tak neco chybi v pameti - TODO
        return f"""Name: {self.name}"
Long: {self.long}, Lat: {self.lat}"""

c1 = City("Prague", 20, 30)
print(c1)