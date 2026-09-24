class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        pop top two, break, push, check conditions, return
        """
        smashingStones = [-weight for weight in stones]
        heapq.heapify(smashingStones)

        while len(smashingStones) > 1:
            #on every iteration, we want to pop the largest two, and smash them, then push back to the heap
            #if anything remains
            stone1, stone2 = heapq.heappop(smashingStones), heapq.heappop(smashingStones)
            rem = -stone1 --stone2
            if rem: heapq.heappush(smashingStones, -rem)
        

        return -smashingStones[0] if smashingStones else 0
