class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        starting from either i = 0 or i = 1,
        return min of those 
        """

        if len(cost) <= 2:
            return min(cost)

        dp = [0] * len(cost)
        dp[0] = cost[-1]
        dp[1] = cost[-2]

        for i in range(2, len(dp)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[-i-1]
        
        print(dp)
        return min(dp[-1], dp[-2])
