# class node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class linkedlist:
#     def __init__(self):
#         self.headval = None

#     def printlist(self):
#         temp = self.headval
#         while temp is not None:
#             print(temp.data, end=" ")
#             temp = temp.next

#     def atbegin(self, newdata):
#         newnode = node(newdata)
#         newnode.next = self.headval
#         self.headval = newnode

#     def atend(self, newdata):
#         newnode = node(newdata)
#         if self.headval is None:
#             self.headval = newnode
#             return
#         tail = self.headval
#         while tail.next is not None:
#             tail = tail.next
#         tail.next = newnode

#     def removenode(self, removekey):
#         temp = self.headval
#         if temp is not None:
#             if temp.data == removekey:
#                 self.headval = temp.next
#                 temp = None
#                 return
#         while temp is not None:
#             if temp.data == removekey:
#                 break
#             previous = temp
#             temp = temp.next
#         if temp == None:
#             return
#         previous.next = temp.next
#         temp = None

#     def inbet(self, previous, newdata):
#         if previous is None:
#             print("previous node is must!")
#             return
#         newnode = node(newdata)
#         newnode.next = previous.next
#         previous.next = newnode


# list = linkedlist()
# list.headval = node("mon")
# e2 = node("tue")
# e3 = node("wed")

# list.headval.next = e2
# e2.next = e3
# list.printlist()

# print("\n")
# list.atbegin("sun")
# list.printlist()
# print("\n")
# list.atend("thur")
# list.printlist()
# print("\n")
# list.inbet(list.headval, "fri")
# list.printlist()
# print("\n")
# list.removenode(None)
# list.printlist()


string = "rajendra"
wanted = "e"
for i in range(0, len(string)):
    if string[i] == wanted:
        print(f"{str(wanted)} found at  {i}")


str = (input("enter your string"))
for i in range(len(str)):
    print("The Character at %d Index Position = %c" % (i, str[i]))
