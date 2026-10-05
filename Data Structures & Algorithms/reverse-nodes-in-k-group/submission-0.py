# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        recurse for the list
        dummy-> head ---->3
        prevg -> head ---> kth
        #reverse
        nextg -> kth.next
        prevg --> kth --> head
        prevg -> head
        is up to k 
        dummy -> 1 ->2
        """
    
        def kth(node, k):
            #return none if not up to k
            count = 0
            cur = node
            while cur and count < k:
                count += 1
                cur = cur.next
            if not cur:
                return False
            return cur
        
        
        dummy = ListNode(0, head)
        prev_g = dummy

        while True:
            kth_node = kth(prev_g, k)
            if not kth_node:
                break

            next_g = kth_node.next
            first_g = prev_g.next

            #reversal:
            cur, prev = first_g, next_g
            while cur != kth_node:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
    
            kth_node.next = prev
            prev_g.next = kth_node
            prev_g = first_g
 


        return dummy.next
