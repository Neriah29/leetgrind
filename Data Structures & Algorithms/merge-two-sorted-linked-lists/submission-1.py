# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        d1, d2 = list1, list2
        dummy = ListNode()
        res = dummy
        


        while d1 and d2:
            if d1.val < d2.val:
                dummy.next = d1
                d1 = d1.next
                dummy = dummy.next
            else:
                dummy.next = d2
                d2 = d2.next
                dummy = dummy.next
        
        if d1:
            dummy.next = d1
            
        elif d2:
            dummy.next = d2
        
        return res.next
