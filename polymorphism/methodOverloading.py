# IN JAVA <<<< when more than one method with the same name is defined in the same class , concept of method overloading is seen.
# IN PYTHON <<<< if the method written such that it can perform more than one task.

class Myclass:
    def sum(self, a=0, b=0, c=0):
        if a != 0 and b != 0 and c != 0:
            print(a+b+c)
        elif a != 0 and b != 0:
            print(a*b)
        else:
            print('atleast two members required')


m = Myclass()
m.sum(10)
