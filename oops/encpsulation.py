# Using OOP in Python, we can restrict access to methods and variables.
#  This prevents data from direct modification which is called encapsulation.
# In Python, we denote private attributes using underscore as the prefix i.e single _ or double __.


class computer:
    def __init__(self) -> None:
        self.__maxprice = 900

    def sell(self):
        print(f"selling price : {self.__maxprice}")

    def setmaxPrice(self, price):
        self.__maxprice = price


c = computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# Here, we have tried to modify the value of __maxprice outside of the class.
# However, since __maxprice is a private variable, this modification is not seen on the output.
# As shown, to change the value, we have to use a setter function i.e setMaxPrice() which takes price as a parameter.

# using setter function
c.setmaxPrice(1000)
c.sell()
