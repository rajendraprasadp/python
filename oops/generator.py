# a generator is a elegant way to writer custom
# iterators in python which makes it eawsy to work with iterators

# def generator(max):
#     n = 2
#     while n <= max:
#         yield n
#         n += 2


# e = generator(10)
# print(next(e))
# print(next(e))
# print(next(e))
# print(next(e))

def gen():
    x, y = 1, 2
    yield(x, y)
    x += 1
    yield(x, y)


g = gen()
print(next(g))
print(next(g))
