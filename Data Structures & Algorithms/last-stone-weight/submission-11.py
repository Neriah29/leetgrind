class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        pop top two, break, push, check conditions, return
        """
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        while len(stones) > 1:
            #on every iteration, we want to pop the largest two, and smash them, then push back to the heap
            #if anything remains
            stone1, stone2 = heapq.heappop(stones), heapq.heappop(stones)
            rem = -stone1 --stone2
            if rem: heapq.heappush(stones, -rem)
        

        return -stones[0] if stones else 0
