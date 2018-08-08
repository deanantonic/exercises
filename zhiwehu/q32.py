"""
Question:
Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
"""


def square_values():
    # I prefer dictionary comprehension over a for loop
    print {num: num ** 2 for num in range(1, 4)}

    # d = {}
    # for num in range(1, 4):
    #     d[num] = num ** 2
    # print d

square_values()
