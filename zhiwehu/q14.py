"""
Question 14
Level 2

Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
seq = raw_input("Enter a sentence containing uppercase and lowercase letters:")
print "UPPER CASE", sum(c.isupper() for c in seq)
print "LOWER CASE", sum(c.islower() for c in seq)
