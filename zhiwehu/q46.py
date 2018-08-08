"""
Question:
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

Hints:

Use map() to generate a list.
Use filter() to filter elements of a list.
Use lambda to define anonymous functions.
"""

someList = [1,2,3,4,5,6,7,8,9,10]
print [i ** 2 for i in someList if i % 2 == 0]

# alternative
# print map(lambda i: i ** 2, filter(lambda x: x % 2 == 0, someList))
