class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        tring to do a dfs where for the one on the left the curr[i] is appended
        """
        res = []
        subset = []

        def dfs(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return
            if total > target or i >= len(nums):
                return 

            subset.append(nums[i])
            dfs(i, subset, total + nums[i])
            subset.pop()
            dfs(i + 1, subset, total)
        
        dfs(0, subset, 0)
        return res