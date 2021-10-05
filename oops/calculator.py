class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"the value of {self.num} square is {self.num **2}")

    def squareroot(self):
        print(f"the value os {self.num} sr is {self.num **0.5}")

    def cube(self):
        print(f"the value of {self.num} cube root is {self.num **3} ")

    @staticmethod
    def greet():
        print("********************helertewrewrewrwerwerwerewrewlo*******************")


hel = Calculator(4)
hel.square()
hel.cube()
hel.squareroot
hel.greet()
