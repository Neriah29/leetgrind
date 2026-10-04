class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, arr):
            if i >= len(nums):
                res.append(list(arr))
                return
            arr.append(nums[i])
            dfs(i+1, arr)
            arr.pop()

            next_i = i+1
            while next_i < len(nums) and nums[next_i] == nums[i]:
                next_i += 1

            dfs(next_i,arr)
        

        
        dfs(0, [])
        return res
