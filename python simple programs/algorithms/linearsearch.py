def unsorted_ls(list, target):
    n = len(list)
    for i in range(0, n):
        if list[i] == target:
            return True
        elif list[i] > target:
            return False
    return False


list = [1, 43, 673, 2, 8, 4, 67, -98]
list.sort()

x = unsorted_ls(list, -98)
if (x == True):
    print(f"value  found")
else:
    print("not found")


#  smallest number in the list
# def smallest(list):
#     small = list[0]
#     for i in list:
#         if i < small:
#             small = i
#     return small


# x = list(map(int, input("enter the list elements").split()))
# print(x)
# print("the smallest value is ", smallest(x))
