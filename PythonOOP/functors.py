# dalsi pokrocilejsi techniky
# v materials.itstep.org je to Kapitola 6

# MAGICMETHOD __call__ -

# FUNCTOR je funkce s vnitrnim stavem, podobne CLOSURE, muze se lip modularizovat a pak se to jenom skladalo pres vnoreni

class WalletFunctor:

    def __init__(self, startCoins=100):
        self.__startCoins = startCoins

    def __call__(self, coins=0):
        return self.__startCoins + coins

    def __str__(self):
        return f"coins: {self.__startCoins}"

w = WalletFunctor(50)

print(w, end=" .... ")
print(w())
print(w(20))



