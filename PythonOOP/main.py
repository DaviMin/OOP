# Zakladam main, ke kteremu potrebuju objekty zvenci

# ted prenasim funkci Fraction ze souboru fraction.py
from fraction import Fraction

f1 = Fraction(1,3)
print(f1)

f2 = Fraction(2,3)
print(f2)

print(f1 == f2)

f3 = f1 + f2

print(f3)

f3 += f2
print(f3)

try:
    f3 += 3
except TypeError:
    print ("pokusil jsi se secist neshodujici se typy")