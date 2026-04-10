class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = -float("inf")
        l = float("inf")
        for i in range(len(prices)):
            l = min(l, prices[i])
            p = prices[i] - l
            maxp = max(p, maxp) 
        return maxp
        

