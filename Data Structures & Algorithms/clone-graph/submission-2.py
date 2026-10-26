"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        so i guess for any cloning problem we want to use a hashmap to map from real to copy
        """
        if not node:
            return None

        old_to_new = {}
        queue = deque([node])
        old_to_new[node] = Node(node.val)
        
        while queue:
            cur = queue.popleft()
            copy = old_to_new[cur]
            for nbr in cur.neighbors:
                if nbr not in old_to_new:
                    old_to_new[nbr] = Node(nbr.val)
                    queue.append(nbr)

                copy.neighbors.append(old_to_new[nbr])

        return old_to_new[node]