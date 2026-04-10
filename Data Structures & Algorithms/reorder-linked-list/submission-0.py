# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = head
        array =[]
        pointer  = head

        while dummy:
            array.append(dummy)
            dummy = dummy.next
        print (array)
    
        l, r = 1, len(array) -1
        flag = False
        while l <= r:
            if flag:
                pointer.next = array[l]
                l += 1
            else:
                pointer.next = array[r]
                r -= 1
            pointer = pointer.next
            flag = not flag
        pointer.next = None

        

                
