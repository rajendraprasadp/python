# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sum(nums))
# for num in nums:
#     print(num)

# print(sum(num for num in nums))

# num_gen = (num for num in nums)


# def nums():
#     nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     for num in nums:
#         yield num


# print(sum(nums()))ra
# for num in nums():
#     print(num)


# num = int(input("enter a  num : "))
# temp = num
# rev = 0
# while(num > 0):
#     dig = num % 10
#     rev = rev*10+dig
#     num = num//10

# if(temp == rev):
#     print("palindrome")
# else:
#     print(":not a palindrome")


# string = "rara"
# str1 = ""
# for i in string:
#     str1 = i+str1
# print(str1)

# if(string == str1):
#     print("palindrome")
# else:
#     print("not a palindrome")


# num = 153
# order = len(str(num))
# temp = num
# sum = 0
# while(temp > 0):
#     dig = temp % 10
#     sum = sum+dig**order
#     temp = temp//10
# if(num == sum):
#     print("armstrong")
# else:
#     print("no")

# num = int(input())
# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print(f"prime {i}")
#             break
#     else:
#         print("not prime")


n = int(input("enter the number"))
n1, n2 = 0, 1

if(n < 1):
    print(n1)
elif(n == 0 or n == 1):
    print(n2)
else:
    print(n1)
    print(n2)
    for i in range(1, n):

        nth = n1+n2
        n1, n2 = n2, nth
        print(n2)
