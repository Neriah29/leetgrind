# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # node = head
        # s = set()
        # while node:
        #     if node in s:
        #         return True
        #     s.add(node)
        #     node = node.next
        # return False

        l, r = head, head

        while r and r.next:
            r = r.next.next
            l = l.next
            if r== l:
                return True
        return False
            
