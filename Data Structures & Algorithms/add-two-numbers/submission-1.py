# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        """
        We are going to solve this the same way we traditionally add
        we add from the left and have something we carry over 
        so what remains is the remainder division then what we carry
        is the integer division
        """

        dummy = ListNode()
        res = dummy

        d1, d2 = l1, l2
        carry = 0

        while d1 or d2 or carry:
            res.next = ListNode()
            res = res.next
            curr = carry
            if d1: 
                curr += d1.val
                d1 = d1.next
            
            if d2:
                curr += d2.val
                d2 = d2.next

            res.val = curr % 10
            carry = curr // 10        



        return dummy.next



        