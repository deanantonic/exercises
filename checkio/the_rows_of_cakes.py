"""
 Someone has decided to bake a load of cakes and place them on the floor. Our robots can't help but try to find a pattern behind the cakes' disposition. Some cakes form rows, we want to count these rows. A row is a sequence of three or more cakes if we can draw a straight line through its centers. The greater row takes up the smaller rows. So if we have a row with 4 cakes, then we have only one row (not 4 by 3).

The cake locations are represented as a list of coordinates. A coordinate is a list of two integers. You should count the rows.

Input: Сoordinates as a list of lists with two integers.

Output: The quantity of rows as an integer.

Precondition: 0 < |coordinates| < 20
∀ x,y ∈ coordinates : 0 ≤ x,y ≤ 10
"""
from itertools import combinations
cross=lambda a,b: (a.conjugate()*b).imag
dot=lambda a,b: (a.conjugate()*b).real

def solve(points):
    h={}
	num=0
	for e in combinations(list(range(len(points))),3):
		if cross(points[e[1]]-points[e[0]],points[e[2]]-points[e[0]])==0:
			a=(e[0],e[1])
			b=(e[0],e[2])
			c=(e[1],e[2])
			entry=None
			if a in h: entry=h[a]
			if b in h: entry=h[b]
			if c in h: entry=h[c]
			if entry==None:
				num+=1
				h[a]=h[b]=h[c]=num
			else:
				h[a]=h[b]=h[c]=entry
	return num

checkio=lambda data: solve([complex(*e) for e in data])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]]) == 2
    assert checkio(
        [[2, 2], [2, 5], [2, 8], [5, 2], [7, 2], [8, 2],
         [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]]) == 6
