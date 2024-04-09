class BankAccount:
    counter = 0 # dodelavane pro pocitani bankovnich uctu
    def __init__(self, deposit=0):
        self._balance = deposit

    def deposit(self, money):
        self._balance += money

    @classmethod
    def add_counter(cls, num): # self tady neni ze chci pocitat VSECHNY ucty, CLS tady jako promenna, ale nad to musim napsat @classmethod
        cls.counter += num
        # TODO dostudovat class method

    @classmethod
    def get_counter(cls, num):
        cls.counter += num

    def withdraw(self, money):
        """
        metoda vytahne pozadovane zdroje z uctu jestli je to mozne
        :param money: pozadovane mnozstvo penez
        :return: jestli se akce povedla
        """
        try:
            if self._balance >= money:
                self._balance -= money
                return money
        except:
            raise ValueError

    def __str__(self):
        return f"na uctu je : {self._balance} penez"

    @staticmethod
    def sayGreetings(): # TODO, staticmethod, u nej nemusime resit SELF, klasicka class co presne znamena