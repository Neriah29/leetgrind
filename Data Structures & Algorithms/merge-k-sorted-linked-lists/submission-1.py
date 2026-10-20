# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#from collections import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        
        
        heap = []
        for i in range(len(lists)):
            node = lists[i]
            if node:
                heapq.heappush(heap,(node.val, i, node))
        
        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        return dummy.next

