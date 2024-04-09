from Bank_accounts import *

b = BankAccount(100) # vklad 100
s = SavingsAccount(b, 50)

print(b)
print(s)

b.deposit(100)
s.deposit(200)

print(b)
print(s)


