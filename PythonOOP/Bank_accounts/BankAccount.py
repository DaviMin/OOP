class BankAccount:
    def __init__(self, deposit=0):
        self._balance = deposit

    def deposit(self, money):
        self._balance += money

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