"""
Question:
Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

Hints:

Use filter() to filter some elements in a list.
Use lambda to define anonymous functions.
"""

someList = [1,2,3,4,5,6,7,8,9,10]
print ",".join(str(i) for i in someList if i % 2 == 0)

# I don't know, I still find comprehensions more elegant
#print filter(lambda i: i % 2 == 0, someList)
