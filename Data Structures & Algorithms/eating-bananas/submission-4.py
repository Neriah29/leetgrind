import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        [1, 4, 3, 2]
        k can theoretically be max(piles)
        we are searching for k such that the total hours spent is <= h
        h 
        we are providing k
        our binary search is between 1 and max(piles)

        [1, 4, 3, 2]

        """

        left, right = 1, max(piles)
        res = float("inf")

        while left <= right:
            cur_rate = (left + right) //2
            cur_hrs = 0
            for ban_idx in range(len(piles)):
                #rate = ban/hr, hrs = ban/rate
                cur_hrs += math.ceil(piles[ban_idx]/cur_rate)
            
            if cur_hrs > h:
                left = cur_rate + 1
            if cur_hrs <= h:
                res = cur_rate
                right = cur_rate - 1

            
        return res

