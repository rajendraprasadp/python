import numpy as np

m = int(input("enter row size\n"))
n = int(input("enter column size\n"))

mat = np.ndarray(shape=(m, n), dtype=int)

print("enter the %d number of elements of %d*%d matrix" % (m*n, m, n))
for i in range(m):
    for j in range(n):
        mat[i][j] = int(input())

print("the  %d*%dmatrix is" % (m, n))
print(mat)
