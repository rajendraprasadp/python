class Parrot:
    # class attribute
    species = "bird"
    # instancve attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age
    # instance methods

    def sing(self, song):
        print(f"{self.name} can sing {song}")

    def dance(self):
        print(f"{self.name} can dancing")


# instantiate the parrot class
blu = Parrot("blu", 10)
woo = Parrot("woo", 15)
# access class attribute
print(blu.species)
print(woo.species)
# access instance attributes
print(blu.age, woo.age)
# call instance methods
print(blu.sing("hi"), blu.dance())
