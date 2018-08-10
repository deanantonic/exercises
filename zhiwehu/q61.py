"""
Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

Hints:

Use unicode() function to convert.
"""

asc = raw_input()
print unicode(asc, "utf-8")
