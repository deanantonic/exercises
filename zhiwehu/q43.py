"""
Question:
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

Hints:

Use if statement to judge condition.
"""

string = raw_input("yes or no?")
print "Yes" if string in ("yes", "YES", "Yes") else "No"
