"""
Question:

Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.



Hints:
Use random.sample() to generate a list of random values.
"""
import random
print random.sample(xrange(100, 201), 5)
