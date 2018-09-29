"""
 You have been given two anagrams as a string, separated by dash. You need to rearrange the letters to turn the first word into the second. The tools you have for this mission are two stacks and a one-letter buffer. The first stack is the beginning of a word; the second stack is where you will put the anagram. The word is placed in the stack, letter by letter. The first letter of the anagram is placed in the bottom stack and the last letter in the middle stack, until it is needed as the end of the anagram. You need to return the shortest sequence of actions to move and turn the word in the first stack into the anagram in the second. The first stack is labeled 1, the second is labeled 2, and the buffer as 0. The action is written as a string of two numbers which signify the original location of the letter and the new location. For example: 12 means that from the first stack, we take the last letter and place it at the end of the second stack. For the result, you need to get a string that lists the steps, separated by commas.

Input: Two words separated by dash as a string.

Output: A sequence of actions as a string.

Precondition: 1 ≤ |word| < 10
Words contains only ASCII letters in lowercase.
"""
class Node:
    """mixin class for A*"""
    heuristic = lambda self, goal: 0  #must be monotonic

    def astar(self, goal):
        cl, op, parent, kls = set(), {self}, {}, type(self)
        g, f = {self: 0}, {self: self.heuristic(goal)}

        while op:
            t = min(op, key=f.get)
            op.remove(t)

            if t == goal:
                path = []

                while t is not self:
                    t, way = parent[t]
                    path.append(way)

                path.reverse()
                return path

            cl.add(t)
            for u, way, dist in t.neighbors():
                if u not in cl:
                    gu = g[t] + dist

                    if u not in op or gu < g[u]:
                        parent[u] = t, way
                        g[u] = gu
                        f[u] = gu + u.heuristic(goal)
                        op.add(u)


def checkio(data):
    class ASNode(Node, tuple):
        def heuristic(self, goal):
            res = 0
            for s, g in zip(self[2], goal[2]):
                if s == g:
                    res -= 1
                else:
                    break

            for s, g in zip(self[1], goal[2][::-1]):
                if s == g:
                    res -= 1
                else:
                    break
            return res

        def neighbors(self):
            a, b, c = self
            if a:
                yield ASNode(('', b + a, c)), '01', 1
                yield ASNode(('', b, c + a)), '02', 1
            if b:
                if not a:
                    yield ASNode((b[-1], b[:-1], c)), '10', 1
                yield ASNode((a, b[:-1], c + b[-1])), '12', 1
            if c:
                if not a:
                    yield ASNode((c[-1], b, c[:-1])), '20', 1
                yield ASNode((a, b + c[-1], c[:-1])), '21', 1


    start, finish = data.split('-')
    return ','.join(ASNode(('', start, '')).astar(ASNode(('', '', finish))))
