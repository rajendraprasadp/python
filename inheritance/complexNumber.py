#  (a+bi)(c+di) = (ac-bd) + (ad+bc)i  ......formula


class complex:
    def __init__(self, r, i):
        self.real = r
        self.ima = i

    def __add__(self, c):
        return complex(self.real+c.real, self.ima+c.ima)

    def __mul__(self, c):
        mulreal = self.real*c.real - self.ima*c.ima
        mulima = self.real*c.ima + self.ima*c.real
        return complex(mulreal, mulima)

    def __str__(self):
        return f"{self.real} + {self.ima}i"


c1 = complex(3, 2)
c2 = complex(1, 7)
print(c1)
print(c2)
print(c1+c2)
print(c1*c2)
