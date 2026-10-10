class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, arr, cur):
            if cur == target:
                res.append(arr.copy())
                return

            if i >= len(candidates) or cur > target:
                return 
            
            arr.append(candidates[i])
            dfs(i+1, arr, cur + candidates[i])
            arr.pop()
            
            next_i = i+1
            while next_i < len(candidates) and candidates[i] == candidates[next_i]:
                next_i += 1
            
            dfs(next_i, arr, cur)
        
        dfs(0, [], 0)

        return res