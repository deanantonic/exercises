"""
Question:
Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.

Hints:

Use len() function to get the length of a string
"""


def print_max_len(a, b):
    print max(a, b, key=len) if len(a) != len(b) else "{}\n{}".format(a, b)


print_max_len("long", "longer")
