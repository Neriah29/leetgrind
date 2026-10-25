"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        i am thinking of a kind of dfs for the problem
        """
        if not node:
            return None

        cur = Node(node.val)
        p = node

        visited = set()

        def dfs(p, cur):
            if p in visited:
                return
            visited.add(p)
            for nbr in p.neighbors:
                if nbr not in visited:
                    dummy_nbr = Node(nbr.val)
                    cur.neighbors.append(dummy_nbr)
                    dummy_nbr.neighbors.append(cur)
                    dfs(nbr, dummy_nbr)
            
        dfs(p, cur)
        return cur

