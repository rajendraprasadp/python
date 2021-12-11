class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(
            f"Thw name of the the programmer is {self.name} and the product is {self.product}")


raju = Programmer("raju", "microsoft")
noob = Programmer("noob", "github")
raju.getInfo()
noob.getInfo()
