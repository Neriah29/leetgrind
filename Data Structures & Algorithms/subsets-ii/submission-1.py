class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        
        def dfs(i, sub):
            if i >= len(nums):
                res.add(tuple(sub))
                return

            sub.append(nums[i])
            dfs(i+1, sub)
            
            sub.pop()
            dfs(i+1, sub)

        dfs(0, [])
        return [list(tpl) for tpl in res]