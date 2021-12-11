# def bubblesort(seq):
#     n = len(seq)
#     for i in range(n-1):
#         for j in range(0, n-i-1):
#             if seq[j] > seq[j+1]:
#                 seq[j], seq[j+1] = seq[j+1], seq[j]


# x = list(map(int, input().split()))
# print("list before sorting", x)
# bubblesort(x)
# print("list after sorting", x)


# Optimized Bubble sort in Python

def bubbleSort(array):

    # loop through each element of array
    for i in range(len(array)):

        # keep track of swapping
        swapped = False

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:

                # swapping occurs if elements
                # are not in the intended order
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

                swapped = True

        # no swapping means the array is already sorted
        # so no need for further comparison
        if not swapped:
            break


data = [-1, -2, -3]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)
