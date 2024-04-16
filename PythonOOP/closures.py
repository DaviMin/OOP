

# closures funkce - muzeme delat funkce ve funkcich a pak vracet returnem
# TODO problematika scopes
# muze to byt prave o tom, ze si tvorim funkci s datam z jineho souboru
# tohle uz jsou pokrocilejsi techniky


def counter():
    number = 0

    def increment():
        nonlocal number # vnorena funkce NONLOCAL znamena ze to je nelokalni number, tady o rad vyse

                        # neni pak numbr jako number, kazdy ma sve misto v pameti

        number += 1
        return number

    return increment  # obaluje tu vnitrni funkci, vracim increment

c = counter()

print(c)
print(c()) # vola se increment v c, jsou to zanořené funkce
print(c())
print(c())
print("TADY: ", counter()())
print("TADY: ", counter()())

# rozdilny vysledky kvuli zavorkam - increment se tvori nanovo, proto je +1
def print_Hello():
    print("hello")
    return "return" # tady vracim text

pozdrav = print_Hello() # kdyz jsou zavorky, volam funkci, tj print z te funkce
pozdrav2 = print_Hello # v promenne se nachazi funkce a odkaz na cestu k ni v pameti

print(pozdrav)
print(pozdrav2)

pozdrav2() # vzal jsem celou tu funkci
print_Hello()