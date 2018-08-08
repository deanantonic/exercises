"""
Write a function to compute 5/0 and use try/except to catch the exceptions.

Hints:

Use try/except to catch exceptions.
"""


def foo():
    return 5 / 0


try:
    foo()
except ZeroDivisionError:
    print "Can't divide by zero."
except Exception:
    print "Caught an exception."
