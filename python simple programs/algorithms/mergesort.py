def mergeSort(arr):
    if len(arr) > 1:
        point = len(arr)//2
        l = arr[:point]
        m = arr[point:]
        mergeSort(l)
        mergeSort(m)
        i = j = k = 0

        while(i < len(l) and j < len(m)):
            if l[i] < m[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = m[j]
                j += 1
            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(m):
            arr[k] = m[j]
            j += 1
            k += 1


x = list(map(int, input().split(" ")))
print("before", x)
mergeSort(x)
print("after", x)
