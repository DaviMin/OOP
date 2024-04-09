# zadani - bankovni ucty a typy uctu
# vytvorime zakladni trodu BankAccount s atributama jako balance a metodami jako deposit() a withdraw()
# potom vytvorime podtridy jako SavingAccount, CheckingAccount, ktere sdedi vlastnosti a metody z BankAccount
# a mohou mit specificke operace pro dany typ uctu
#

# kdyz se v tech dilcich class def daji """""", tak je zvykem tam psat co to dela, jakej je vystup a pod - Pychar uz neco nabidne
# jsou to tzv dokumentacni retezce


from .BankAccount import BankAccount
from .SavingAccount import SavingsAccount