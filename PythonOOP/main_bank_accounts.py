from Bank_accounts import *

b = BankAccount(100) # vklad 100
b2 = BankAccount(200)
s = SavingsAccount(b, 50)

print(b.counter)
print(s)

b.deposit(100)
s.deposit(200)

print(b)
print(s)


