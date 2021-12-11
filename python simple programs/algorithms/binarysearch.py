def binarysearcha(theValues, target):
    low = 0
    high = len(theValues)-1
    while low <= high:
        mid = (low+high)//2
        if(theValues[mid] == target):
            return True
        elif target < theValues[mid]:
            high = mid-1
        else:
            low = mid+1

    return False


y = [int(x) for x in input("enter the klist elements : ").split()]
print(y)
v = binarysearcha(y, 5)
if (v == True):
    print("value founr")
else:
    print("value not found")
