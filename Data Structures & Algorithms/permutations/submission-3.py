class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(i):
            if i == -1:
                return [[]]
            cur = []
            for arr in dfs(i-1):
                for pos in range(len(arr)+1):
                    dummy = arr.copy()
                    dummy.insert(pos, nums[i])
                    cur.append(dummy)
            return cur
        
        return(dfs(len(nums)-1))
        
                    


