# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        dummy = curr
        tot = 0
        while curr:
            curr = curr.next
            tot += 1
        counter = tot - n
        #case of first node
        if counter == 0:
            head = head.next
        #case of any other node
        else:
            c = 0
            while c < counter-1:
                dummy = dummy.next
                c += 1
            r = dummy.next 
            dummy.next = dummy.next.next
            r.next = None
        return head
            

