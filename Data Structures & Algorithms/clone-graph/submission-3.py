"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clones = {}
        clones[node] = Node(node.val)
        queue = deque([node])
        while queue:
            curNode = queue.popleft()
            curClone = clones[curNode]
            for nbr in curNode.neighbors:
                if nbr not in clones:
                    clones[nbr] = Node(nbr.val)
                    queue.append(nbr)
                curClone.neighbors.append(clones[nbr])


        return clones[node]