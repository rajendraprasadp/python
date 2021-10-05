class Train:

    def __init__(self, name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare

    def bookTicket(self):
        if(self.seats > 0):
            print(f"thanks for booking! num={self.seats}")
            self.seats = self.seats - 1
        else:
            print("no seats! ")

    def getStatus(self):
        print(
            f"the name of the train is {self.name} and seats avialable are{self.seats}")

    def fareInfo(self):
        print(f"the price of the fare is {self.fare}")


express = Train("govinda express", 300, 1234)
express.getStatus()
express.fareInfo()
express.bookTicket()

express.bookTicket()
