class Calculator: # chci jen 1 kalkulacku, proto se to resi individ, neni tam __init__
    ans = 0
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def divide(self, a, b):
        return a / b

    @classmethod
    def ans_add(cls, a):
        cls.ans += a
        return cls.ans

    @classmethod
    def clean_ans(cls): # timto vymazu posledni vysledek
        cls.ans = 0

# TODO nastudovat rozdil mezi staticmethod a classmethod (obe jsou bez self), nazývají se dekorátor