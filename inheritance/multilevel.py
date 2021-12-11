
class animals:
    animal = "mammal"


class pet:
    color = "white"


class cat():

    # both are giving the same output , one with static method and other with just using self....
    def speak(self):
        print("********meow meow*******")

    @staticmethod
    def speak():
        print("********meow meow*******")


c = cat()
c.speak()
