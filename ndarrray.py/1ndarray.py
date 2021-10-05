import numpy

n = int(input("enter the size of the array\n"))
arr = numpy.ndarray(shape=(n), dtype=int)


print("Enter the %d elements" % n)
for i in range(n):
    arr[i] = int(input())

print("array elements", arr)
