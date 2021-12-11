import math
# 1.LIST COMPREHENSION

numbers = [2**i for i in range(6)]

# returning a list of square roots of even elements of input list
x = list(map(int, input().split(" ")))
newlist = [math.sqrt(i) for i in x if i % 2 == 0]
print(newlist)

# 2.SET COMPREHENSION

a = "programming"
b = {x for x in a}
print(b)

# 3.DICTIONARY COMPREHENSION

# increase the price of items in dictionary by 1.5 for those
# whose current price is greater than 2.0

oldprice = {'milk': 1.02, "coffee": 2.5, "bread": 2.5}
newprice = {key: value*1.5 if value >
            2.0 else value for (key, value) in oldprice.items()}
print(newprice)
