# class polygon:
#     def __init__(self, sides):
#         self.sides = sides

#     def display(self):
#         print("polygon")

#     def get_perimeter(self):
#         perimeter = sum(self.sides)
#         return perimeter


# class triangle(polygon):

#     def display(self):
#         print("triangle")
#         super().display()


# class quad(polygon):
#     def display(self):
#         print("quad")


# t = triangle([5, 6, 7])
# perimeter = t.get_perimeter()
# print(perimeter)

# t.display()


class bird:
    def __init__(self) -> None:
        print("bird id ready")

    def swim(self) -> None:
        print("swim is easy")


class parrot(bird):
    def __init__(self) -> None:
        super().__init__()
        print("parrot id ready")


# The child class inherits the functions of parent class. We can see this from the swim() method.
p = parrot()
p.swim()
