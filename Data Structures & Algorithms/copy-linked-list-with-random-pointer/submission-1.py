"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old = head
        oldToNew = {None:None}
        while old:
            copy = Node(old.val)
            oldToNew[old] = copy
            old = old.next
        
        old = head
        while old:
            copy = oldToNew[old]
            copy.next = oldToNew[old.next]
            copy.random = oldToNew[old.random]
            old = old.next
        return oldToNew[head]


        
