"""
Question:
Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

Hints:

Use % operator to check if a number is even or odd.
"""


def even_or_odd(n):
    print "It is an even number" if n % 2 == 0 else "It is an odd number."


even_or_odd(4)
even_or_odd(5)
