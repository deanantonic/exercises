"""
 You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.

For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).

Input: A positive integer.

Output: The product of the digits as an integer.

Precondition: 0 < number < 106
"""


def checkio(number: int) -> int:
    nonZero = [int(i) for i in str(number) if int(i) != 0]
    product = 1
    for i in nonZero:
        product *= i
    return product

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")




# alternative with functools and operator
# from functools import reduce
# from operator import mul
# def checkio(number: int) -> int:
#     nonZero = [int(i) for i in str(number) if int(i) != 0]
#     return reduce(mul, nonZero)


# or a clever one
# def checkio(number: int) -> int:
#     nonZero = [int(i) for i in str(number) if int(i) != 0]
#     eval('*'.join(str(item) for item in nonZero))
