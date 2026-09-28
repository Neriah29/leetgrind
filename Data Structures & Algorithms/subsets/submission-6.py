class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(arr, i):
            nonlocal res
            #base case
            if i >= len(nums):
                res.append(arr.copy())
                return 
            
            arr.append(nums[i])
            dfs(arr, i+1)
            arr.pop()
            dfs(arr, i + 1)

        dfs([], 0)
        return res
        

        

