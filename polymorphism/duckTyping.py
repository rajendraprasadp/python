# if a variable or object or method perform different behaviour according to the situation , it is called polymorphism
class duck:
    def walk(self):
        print("quack quack")


class horse:
    def walk(self):
        print("thbak thabak")


class horse2:
    def walkr(self):
        print("thbak thabak")

# common interface


def myfunc(x):
    if hasattr(x, "walk"):   # strong typing to avoid error
        x.walk()


# instantiate objects
d = duck()
h = horse()
z = horse2()

# passing the object
myfunc(d)
myfunc(h)
myfunc(z)
