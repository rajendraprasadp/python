# Python 3 program to find
# factorial of given number
import math


def factorial(n):
    # if n < 0:
    #     return 0
    # elif n == 0 or n == 1:
    #     return 1
    # else:
    #     fact = 1
    #     for i in range(1, n+1):
    #         fact *= i
    #     return fact

    return 1 if(n == 0 or n == 1) else n*factorial(n-1)
    return (math.factorial(n))


num = 5
print("Factorial of", num, "is",
      factorial(num))
print(f"factoraial of {num} is {factorial(num)}")
