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
        copyDict ={None: None}
        curr = head
        while curr:
            copy = Node(curr.val)
            copyDict[curr] = copy 
            curr = curr.next
        
        curr = head

        while curr:
            copy = copyDict[curr]
            copy.next = copyDict[curr.next]
            copy.random = copyDict[curr.random]
            curr = curr.next
            
        return copyDict[head]
        
