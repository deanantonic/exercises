"""
Question 20
Level 3

Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield
"""


class Iterator(object):

    def __init__(self, n):
        super(Iterator, self).__init__()
        self.n = n

    def divBySeven(self):
        for i in range(0, self.n):
            if i % 7 == 0:
                yield i


for num in Iterator(100).divBySeven():
    print num
