"""
Question 16
Level 2

Question:
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

# the question says each odd number should be squared so my solution reflects that even though the author forgot to square the output in the docstring
seq = [int(i) ** 2 for i in raw_input("Enter a sequence of comma-separated numbers:").split(",") if int(i) % 2 != 0]
print ",".join(str(i) for i in seq)
