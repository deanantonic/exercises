"""
Question:

Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

Hint:
Use for loop to iterate all possible solutions.
"""


def inventory(total, numLegs):
    for rabbits in range(total + 1):
        chickens = total - rabbits
        if 2 * chickens + 4 * rabbits == numLegs:
            return chickens, rabbits
    return None, None


print inventory(35, 94)
