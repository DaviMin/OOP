# vytvor tridu s nazvem MathFunctor, ktera bude obsahovat 1 atribut operation
# v tride MathFunctor vytvor konstruktor, ktery bude prijimat 1 parametr operation (napr add, substract, multiply, divide)
# implemtuj metodu __call__  (self,a,b), ktera bude vykonavat ioperaci podle hodnoty operation na cislecha a a b vysledek operac evratte
# vytvorte instanci tridy MathFunctor pro ruzne operace (+, -, x, /)
# pouzijte vytvorene funktory na matematicke operace s ruznymi cisly


class MathFunctor:
    def __init__(self, operation):
        self.operation = operation

    def __call__(self, a, b):
        if self.operation == "add":
            return a + b
        elif self.operation == "subtract":
            return a - b
        elif self.operation == "multiply":
            return a * b
        elif self.operation == "divide":
            if b != 0:
                return a / b
            else:
                raise ValueError("Division by zero is not allowed.")
        else:
            raise ValueError("Invalid operation.")






add_functor = MathFunctor("add")
subtract_functor = MathFunctor("subtract")
multiply_functor = MathFunctor("multiply")
divide_functor = MathFunctor("divide")

result1 = add_functor(5, 3)
result2 = subtract_functor(10, 4)
result3 = multiply_functor(7, 2)
result4 = divide_functor(12, 3)

print(result1)
print(result2)
print(result3)
print(result4)
print()

#MRO je na poradi dedeni, kdyz dedim z vicero objektu
print(MathFunctor.mro())
print(type(add_functor))
print(type(subtract_functor))
print()

t = [add_functor, subtract_functor, add_functor] # tohle je nejaky seznam jak to udelat
nums = [2, 4, 5]

num = 10
for i in range(3):
    num = t[i](num, nums[i])

print(num)

# a pak s epodivat na DECORATOR, ten je treba dobry @autorization, takze pusti jenom kdyz bude autorizovanej


