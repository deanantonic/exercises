"""
Question:

Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

10

Then, the output of the program should be:

0,2,4,6,8,10

Hints:
Use yield to produce the next value in generator.

In case of input data being supplied to the question, it should be assumed to be a console input.
"""
n = int(raw_input("Enter a number:"))


def foo(n):
    for num in (i for i in range(n+1) if i % 2 == 0):
        yield num


generated = []
for x in foo(n):
    generated.append(x)

print ",".join(str(i) for i in generated)
