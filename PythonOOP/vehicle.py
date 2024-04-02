# OOP obsahuje objektty, budou se s tim rezit polymorfie, dedicnost apod...
# Objekty jsou takove datove typy
# Class - budeme vyrabet datove typy jako auto, cloveka, stroj

class Vehicle: # tridy jsou zvykle psat s velkym pismenem
    def __init__(self, name): # __ znamenaji magic neco - TODO, self znamena, ze se odkazuje smao na sebe
        # __init__ inicializace konkretniho objektu podle Classu
        self.name = name # ulozi se do vlastniho self jmena - bezna praxe

    # ted aby to neco umelo - treba nastartovat
    def start(self): # typicke pro Python tohleti self, chce to explicitne vypsane, v jinych ne
        print(f"brmbrm startuju vozidlo {self.name}")


# ukazu si na 3 objektech - Vehicle
v1 = Vehicle("Vehicle1") # list ()
v2 = Vehicle("Vehicle2")
v3 = Vehicle("Vehicle3")

print(v1.name)
print(v2.name)
print(v3.name)
print(type(v1)) # to abych si prekontroloval co je to v1, jaky je to datovy typ
v2.start() # tady self uz neresim