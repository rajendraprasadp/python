def selectionsort(seq):
    n = len(seq)
    for i in range(n-1):
        smallndx = i
        for j in range(i+1, n):
            if(seq[j] < seq[smallndx]):
                smallndx = j
        seq[i], seq[smallndx] = seq[smallndx], seq[i]


y = [int(x) for x in input().split()]
print("before sorting", y)
selectionsort(y)
print("after sorting", y)
