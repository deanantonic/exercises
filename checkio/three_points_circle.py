"""
 Nicola discovered a calliper inside a set of drafting tools he received as a gift. Seeing the caliper, he has decided to learn how to use it.
Through any three points that do not exist on the same line, there lies a unique circle. The points of this circle are represented in a string with the coordinates like so:
    "(x1,y1),(x2,y2),(x3,y3)"
Where x1,y1,x2,y2,x3,y3 are digits.
You should find the circle for three given points, such that the circle lies through these point and return the result as a string with the equation of the circle. In a Cartesian coordinate system (with an X and Y axis), the circle with central coordinates of (x0,y0) and radius of r can be described with the following equation:
    "(x-x0)^2+(y-y0)^2=r^2"
where x0,y0,r are decimal numbers rounded to two decimal points. Remove extraneous zeros and all decimal points, they are not necessary. For rounding, use the standard mathematical rules.
Input: Coordinates as a string..
Output: The equation of the circle as a string.
Precondition: All three given points do not lie on one line.
0 < xi, yi, r < 10
"""
import math


def checkio(s):
    s = s.replace("(", " ")
    s = s.replace(",", " ")
    s = s.replace(")", " ")
    l = s.split(' ')
    n = []
    for i in l:
        if len(i) != 0:
            n.append(int(i))
    a = 2*(n[2]-n[0])
    b = 2*(n[3]-n[1])
    c = n[2]*n[2]+n[3]*n[3]-n[0]*n[0]-n[1]*n[1]
    d = 2*(n[4]-n[2])
    e = 2*(n[5]-n[3])
    f = n[4]*n[4]+n[5]*n[5]-n[2]*n[2]-n[3]*n[3]
    x = (b*f-e*c)/float((b*d-e*a))
    y = (d*c-a*f)/float((b*d-e*a))
    r = math.sqrt((x-n[0])*(x-n[0])+(y-n[1])*(y-n[1]))
    x = round(x, 2)
    if x == int(x):
        x = int(x)
    y = round(y, 2)
    if y == int(y):
        y = int(y)
    r = round(r, 2)
    if r == int(r):
        r = int(r)
    return "(x-"+str(x)+")^2+(y-"+str(y)+")^2="+str(r)+"^2"


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
