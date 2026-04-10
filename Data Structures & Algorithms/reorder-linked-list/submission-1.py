# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        array = []
        begin = False 
        d1 = head.next
        while d1:
            array.append(d1)
            d1 = d1.next

        print(array)
        curr = head
        l, r = 0, len(array) -1 
        while l <= r:
            if begin:
                curr.next = array[l]
                curr = curr.next
                l += 1
                begin = False
            else:
                curr.next = array[r]
                curr = curr.next
                r -= 1
                begin = True
        curr.next = None
        

