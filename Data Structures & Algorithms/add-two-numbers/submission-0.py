# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1, h2 = l1, l2
        num1, num2 = "", ""
        while h1:
            num1 += str(h1.val)
            h1 = h1.next
        
        while h2:
            num2 += str(h2.val)
            h2 = h2.next
        
        num1, num2 = int(num1[::-1]), int(num2[::-1])
        num3 = str(num1 + num2)[::-1]
        dummy = ListNode()
        tail = dummy
        for i in range(len(num3)):
            tail.next = ListNode(int(num3[i]))
            tail = tail.next
        return dummy.next

