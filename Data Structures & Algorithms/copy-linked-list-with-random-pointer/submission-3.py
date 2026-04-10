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
        if not head:
            return None
        
        #we use a dictionary to map each real nide to its copy 
        curr = head
        copyMap = {}
        while curr:
            copyMap[curr] = Node(curr.val)
            curr = curr.next

        
        for real, copy in copyMap.items():
            if real.next:
                copy.next = copyMap[real.next]
            if real.random:
                copy.random = copyMap[real.random]

        return copyMap[head]

