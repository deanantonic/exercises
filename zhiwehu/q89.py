"""
Question:

With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.

Hints:
Use set() and "&=" to do set intersection operation.
"""
nums1 = set([1, 3, 6, 78, 35, 55])
nums2 = set([12, 24, 35, 24, 88, 120, 155])
nums1 &= nums2
intersect = list(nums1)
print "NUMS1", nums1
print intersect
