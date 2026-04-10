class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        profit = 0
        for price in prices:
            min_price = min(min_price, price)   
            cur_prof = price - min_price
            profit = max(profit,cur_prof)
        return profit