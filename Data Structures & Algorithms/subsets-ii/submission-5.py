class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, cur):
            if i >= len(nums):
                res.append(cur.copy())
                return

            cur.append(nums[i])
            dfs(i+1, cur)    
            cur.pop()
            next_i = i+1

            while next_i < len(nums) and nums[i] == nums[next_i]:
                next_i += 1

            dfs(next_i, cur)
        
        dfs(0, [])
        return res