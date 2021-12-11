# if any operator performs additional operations other than wants it meant for, it is called is OPERATOR OVERLOADING
class A:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x+other.x


class B:
    def __init__(self, x):
        self.x = x


a = A(100)
b = B(200)

print(10+20)
print(int.__add__(10, 20))  # same as previous statement

print("10"+"20")
print(str.__add__("10", "20"))

print(a+b)
print(A.__add__(a, b))

# here the same operator '+' is used for different operations!
