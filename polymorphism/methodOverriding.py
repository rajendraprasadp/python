# is used when proogrammer wants to modify the existing behaviour of the method
class add:
    def addition(self, x, y):
        print("adition is : ", x+y)


class multiply(add):
    def multi(self, x, y):
        super().addition(x, y)
 # by caling super we can access parent class method and no need to create 2 objects to access both methods
        print("multiplication is : ", x*y)


# a = add()
# a.addition(1, 3)
m = multiply()
m.addition(2, 4)
m.multi(2, 4)
