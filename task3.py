class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.num = numerator
        self.den = denominator

    def __add__(self, other):
        return Fraction(self.num * other.den + other.num * self.den, self.den * other.den).short()

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den).short()

    def __sub__(self, other):
        return Fraction(self.num * other.den - other.num * self.den, self.den * other.den).short()

    def __truediv__(self, other):
        return self.__mul__(Fraction(other.den, other.num)).short()

    def short(self):
        mcm = self.num
        while mcm > 1:
            if self.num % mcm == 0 and self.den % mcm == 0:
                return Fraction(int(self.num / mcm), int(self.den / mcm))
            mcm -= 1
        return self

    def __str__(self):
        return f"{self.num}/{self.den}"


"""
Task 3

Fraction

Create a Fraction class, which will represent all basic arithmetic logic for fractions (+, -, /, *) with appropriate checking and error handling

```

class Fraction:

pass

x = Fraction(1/2)

y = Fraction(1/4)

x + y == Fraction(3/4)
"""
