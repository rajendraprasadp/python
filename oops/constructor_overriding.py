# constructor overriding is used when programmer wants to  modify the existing behaviour of the constructor.
class father:
    def __init__(self):
        self.money = 1000
        print("father class constructor")


class son(father):
    def __init__(self, a):
        # how can we call parent class constructor?
        super().__init__()  # calling parent class constructor
        self.money = a
        print("son class constructor")


s = son(10)
print(s.money)
