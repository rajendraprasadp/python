# larger= lambda a,b: a if a>b else b
# print(larger(1,2))


num = [1, 2, 3, 4, 5]

# map() function applies given condiiton to each item of the iterable

squared = map(lambda n: n**2, num)
print(list(squared))

# filter() function filters out elements based on the condition specified

onlyeven = filter(lambda n: n % 2 == 0, num)
print(list(onlyeven))
