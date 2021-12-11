# def area(r):
#     PI = 3.142
#     return PI * (r*r)


# print(area(5))
# print("the area os circle is %.6f" % area(5))

# second largest number in list by input provided by user

# list = []
# num = int(input('enter the number of elements in the list:'))

# for i in range(1, num+1):
#     ele = int(input(f"enter the {num} elements"))
#     list.append(ele)

# print("the second largest num is ", sorted(list)[-2])


def maxlist(list):
    max = list[0]

    for x in list:
        if x > max:
            max = x
    return max


m = int(input("Enter number of elements : "))
x = list(map(int, input().split()))
print("list is ", x)

# # x = list(map(int, input("Enter a multiple value: ").split()))
# # x = [int(x) for x in input().split()]
print("the largest number is ", maxlist(x))
