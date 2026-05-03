class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        thought process
        given: [0,10,3,4,2,3]
        heapify
        while len(heap)>1:
            run the major function
        return heap if heap else 0
        """

        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1: #O(n)
            one = heapq.heappop(maxHeap)
            two = heapq.heappop(maxHeap)   
            if one == two:
                continue
            heapq.heappush(maxHeap, one - two)      
        
        return -maxHeap[-1] if maxHeap else 0



