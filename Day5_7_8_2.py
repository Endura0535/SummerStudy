class Fraction:
    numerator = 0
    denominator = 0
    def __init__(self, numerator, denominator):
         self.numerator = numerator
         self.denominator = denominator

    def __add__(self, other):
        a = other.numerator*self.denominator+other.denominator*self.numerator
        b = other.denominator*self.denominator
        i = 1
        while i < a + 1 or i < b + 1:
            if a % i == 0 and b % i == 0:
                c = a / i
                d = b / i
            i = i + 1
        print str(c) + "/" + str(d)

    def __sub__(self, other):
        a = other.numerator*self.denominator-other.denominator*self.numerator
        b = other.denominator*self.denominator
        i = 1
        while i < a + 1 or i < b + 1:
            if a % i == 0 and b % i == 0:
                c = a / i
                d = b / i
            i = i + 1
        print str(c) + "/" + str(d)

    def __mul__(self, other):
        a = self.numerator*other.numerator
        b = self.denominator*other.denominator
        i = 1
        while i < a + 1 or i < b + 1:
            if a % i == 0 and b % i == 0:
                c = a / i
                d = b / i
            i = i + 1
        print str(c) + "/" + str(d)

    def __truediv__(self, other):
        a = self.numerator*other.denominator
        b = self.denominator*other.numerator
        i = 1
        while i < a + 1 or i < b + 1:
            if a % i == 0 and b % i == 0:
                c = a / i
                d = b / i
            i = i + 1
        print str(c) + "/" + str(d)


frac = Fraction(2, 9)
frac2 = Fraction(4, 9)
frac.__add__(frac2)
frac.__sub__(frac2)
frac.__mul__(frac2)
frac.__truediv__(frac2)