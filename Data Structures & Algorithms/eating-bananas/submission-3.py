import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
#do a binary search from 0 to the max(piles):
#check if t > h reduce, else increase it. keep going 

        #initialize left and right pointers:
        l, r = 1, max(piles)

        res = max(piles)
        while l <= r:
            m = (l + r)//2

            time = 0
            for i in range(len(piles)):
                time += math.ceil(piles[i]/ m)
            if time <= h:
                r = m - 1
                res = min(res, m)
            else:
                l = m + 1
        return res