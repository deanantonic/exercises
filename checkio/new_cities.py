"""
 Sometimes damaged nodes are unrecoverable. In that case, people that were connected to the crushed node must migrate to another district while administration attempts to fix the node.

But if a crushed node disconnects multiple districts from one another, then the network splits into two sub-networks and every sub-network should have their own Mayor. And Mayors must use pigeons for mailing between each other. In that case, when the network is split you don’t need hundreds of pigeons.

Your mission is to figure out how many Mayors you need to control the entire city when some nodes are crushed. In other words, you need to figure out how many sub-networks will be formed after some nodes are crush and not recovered.

Input: Two arguments: the network structure (as a list of connections between the nodes) and the list of crashed nodes.

Output: Int. The amount of sub-networks formed after some nodes were crushed.
"""
def subnetworks(net, crushes):
    crushes = set(crushes)
    cities = 0
    visited = set()

    alive = set()
    for connection in net:
        for node in connection:
            if node not in crushes:
                alive.update(node)

    for start in alive:
        if start not in visited:
            stack = {start}
            while stack:
                current = stack.pop()
                visited = visited | {current}
                for left, right in net:
                    if right == current:
                        if left not in visited and left not in crushes:
                            stack = stack | {left}
                    elif left == current and (right not in visited and right not in crushes):
                        stack = stack | {right}
            cities = cities + 1
    return cities

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['B']) == 2, "First"
    assert subnetworks([
            ['A', 'B'],
            ['A', 'C'],
            ['A', 'D'],
            ['D', 'F']
        ], ['A']) == 3, "Second"
    assert subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['C', 'D']) == 1, "Third"
    print('Done! Check button is waiting for you!')
