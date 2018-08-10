"""
Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].

Hints:
Use list comprehension to delete a bunch of element from a list.
"""
nums = [5, 6, 77, 45, 22, 12, 24]
print [i for i in nums if i % 2 != 0]
