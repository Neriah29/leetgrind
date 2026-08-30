class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        on every iteration
        we will have:
        curMin
        curMaxProfit
        """

        curMin = prices[0]
        maxProfit = curMaxprofit = 0

        for i in range(len(prices)):
            curProfit = prices[i] - curMin
            maxProfit = max(curProfit, maxProfit)
            curMin = min(curMin, prices[i])
        
        return maxProfit


