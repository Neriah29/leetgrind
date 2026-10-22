class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1,1]

        for i in range(2,n+1):
            cur = sum(dp)
            dp[0], dp[1] = dp[1], cur
    
        return dp[1]