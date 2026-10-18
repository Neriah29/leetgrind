class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        the 
        """
        def robber(nums):
            if len(nums) <= 2:
                return max(nums)
            
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            
            return dp[-1]

        
        if len(nums) <= 2:
            return max(nums)
        return max(robber(nums[1:]), robber(nums[:-1]))
