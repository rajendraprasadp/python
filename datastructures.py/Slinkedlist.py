class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SlinkedList:
    def __init__(self):
        self.headval = None

    def printlist(self):
        temp = self.headval
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next

    def atbegin(self, newdata):
        newnode = Node(newdata)
        newnode.next = self.headval
        self.headval = newnode

    def atend(self, newdata):
        newnode = Node(newdata)
        if self.headval is None:
            self.headval = newnode
            return
        tail = self.headval
        while(tail.next is not None):
            tail = tail.next
        tail.next = newnode

    def removenode(self, removekey):
        temp = self.headval

        if(temp is not None):
            if(temp.data == removekey):
                self.headval = temp.next
                temp = None
                return

        while(temp is not None):
            if(temp.data == removekey):
                break
            previous = temp
            temp = temp.next

        if(temp == None):
            return

        previous.next = temp.next
        temp = None

    def inbet(self, mn, newdata):
        if (mn is None):
            print("no middlenode")
            return
        newnode = Node(newdata)
        newnode.next = mn.next
        mn.next = newnode


list = SlinkedList()
list.headval = Node("mon")
n2 = Node("tue")
n3 = Node("wed")

list.headval.next = n2
n2.next = n3

list.printlist()
print("\n")
list.atbegin("sun")
list.printlist()
print("\n")
list.atend("thur")
list.printlist()
print("\n")
list.inbet(list.headval, "nsklandlknaslkfd")
list.printlist()
list.removenode("wed")
print("\n")
list.printlist()
