# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        countCheck = head
        count = 0
        while countCheck:
            countCheck = countCheck.next
            count += 1
        print(count)
        
        #count is the number of nodes in it and it has to be >2
        toGoTo = count - n + 1
        
        curr = 1
        run = head
        if toGoTo > 1:
            while curr < toGoTo -1:
                run = run.next
                curr += 1
            rem = run.next
            run.next = run.next.next
            rem.next = None

        else:
            head = head.next
            run.next = None
        
        return head



            