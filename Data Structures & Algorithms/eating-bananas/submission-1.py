class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = math.ceil(sum(piles)/h), max(piles)
        res = max(piles)

        while l <= r:
            k = (l + r)//2
            hr = 0
            for i in piles:
                hr += math.ceil(i/k)
            
            if hr <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k+1
        
        return res
