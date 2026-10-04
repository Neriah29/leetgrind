# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode()
        cur = dummy

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))


        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            node = node.next
            if node:
                heapq.heappush(heap,(node.val, i, node))
        
        return dummy.next