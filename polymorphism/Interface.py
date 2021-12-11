# interface is abstract class which contains only abstruct method ; no single concrete method.
from abc import ABC, abstractmethod


class Father(ABC):  # inteface class
    @abstractmethod
    def disp1(self):
        pass

    @abstractmethod
    def disp2(self):
        pass


class child(Father):  # still an
    def disp1(self):
        print("child class")
        print("disp1 abstruct method")
        print("hllo")


class grandchild(child):
    def disp2(self):
        print("grandchild class")
        print("disp2 abstuct method")


gc = grandchild()
gc.disp2()
gc.disp1()
