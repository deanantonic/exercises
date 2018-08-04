"""
Question 9
Level 2

Question
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
seq = []
while True:
    input = raw_input("Input a sequence of lines pressing enter key after each one, when done, simply press enter without typing a line:")
    if input == "":
        break
    seq.append(input.upper())

for elem in seq:
    print elem
