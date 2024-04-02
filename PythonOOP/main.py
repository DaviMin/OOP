# import os


def write_to_file(file_name, data):
    with open(file_name, "w") as file_handler:
        file_handler.write(data)
        # otevru soubor a zapisu

def read_from_file(file_name): # bez dat, ze budu jenom cist
    data = None
    with open(file_name, "r") as file_handler:
        data = file_handler.read()

    return data

if __name__ == '__main__': #TODO zjistit co to je za znamena to, ze s tema podtrzitkama je spousteny jako hlavni soubor
    MY_FILE = "file.txt" #d efinuji si konstantu na vyhrazený soubor (vytvarim si bezne konfiguracni soubor s konstantama)

    user_input = input("zadej zpravu: ")
    write_to_file(MY_FILE, user_input)
    print("Zapis se povedl")

    data = read_from_file(MY_FILE)
    print(data)

# OOP obsahuje objektty, budou se s tim rezit polymorfie, dedicnost apod...
# Objekty jsou takove datove typy
# Class - budeme vyrabet datove typy jako auto, cloveka, stroj