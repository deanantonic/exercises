"""
Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.


Hints:
Use if/elif to deal with conditions.
"""


def binarySearch(array, beginIndex, endIndex, value):
    while (beginIndex < endIndex):
        mid = (beginIndex + endIndex) / 2
        if array[mid] < value:
            beginIndex = mid + 1
        elif array[mid] > value:
            endIndex = mid - 1
        else:
            return mid

    if array[beginIndex] == value:
        return beginIndex
    else:
        return -1


print binarySearch([2, 3, 3, 3, 4, 5], 0, 5, 3)
