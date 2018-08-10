"""
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

Hints:
Use set() to store a number of values without duplicate.
"""
# my favorite solution, needs more_itertools library
from more_itertools import unique_everseen
nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
print list(unique_everseen(nums))



# this is an interesting solution but only for this example, can't rely on it
# print sorted(set(nums), key=nums.index)


# alternative solution
# from collections import OrderedDict
# nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
# unique = list(OrderedDict.fromkeys(nums))
# print unique
