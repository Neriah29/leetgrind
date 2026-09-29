class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        edge case is when the total is above or equal to target 
        we can have a function with i, 

        edge cases:
        i > len, total >= target
        at each i we want to do for the next i 
        """

        res = []

        def dfs(i, total, array):
            if total == target:
                res.append(array.copy())
                return 
            if total >target:
                return
            if i >= len(nums):
                return
            
            array.append(nums[i])
            dfs(i, total + nums[i], array)
            array.pop()
            dfs(i+1, total, array)
        
        dfs(0, 0, [])
        return res
        
