class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone_1 = -heapq.heappop(stones)
            stone_2 = -heapq.heappop(stones)
            if stone_1 - stone_2 > 0:
                heapq.heappush(stones, stone_1 - stone_2)
        
        return stones[0] if stones else 0

