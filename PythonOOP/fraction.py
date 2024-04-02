from my_error import MyCustomError

class Fraction:

    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator

    def __str__(self):
        return f"{self.nominator}/{self.denominator}"

    def __eq__(self, other):
        return self.nominator * other.denominator == self.denominator * other.nominator

    def __add__(self, other):
        common_denominator = self.denominator * other.denominator
        new_nominator = self.nominator * other.denominator + other.nominator * self.denominator
        return Fraction (new_nominator, common_denominator) # vyleze ven objekt, s ekterym budu pracovat v main.py

    def __iadd__(self, other):
        if isinstance(other, Fraction) # jestli je to spravny datovy typ
            common_denominator = self.denominator * other.denominator
            self.nominator = self.nominator * other.denominator + other.nominator * self.denominator
            self.denominator
            return self

        raise TypeError("Unsupported operand type for +=: '{}' and '{}'".format(type(self), type(other)))
    # raise je trochu jine nez try a except, do mainu se vlozi mozne try a except