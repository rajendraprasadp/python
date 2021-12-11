try:
    numer = int(input("enter numerator\n"))
    denom = int(input("enter denominator\n"))
    div = numer/denom
    print(div)

    list = [1, 2, 3]
    i = int(input("enter the index of element you want!"))
    print(list[i])
# Specific error handling methods
except ZeroDivisionError:
    print("denominator cant be zero")
except IndexError:
    print("index out of range")
finally:
    print("finally done!")
