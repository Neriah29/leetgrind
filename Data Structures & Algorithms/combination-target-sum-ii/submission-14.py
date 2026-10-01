class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, arr, cur_sum):
            if cur_sum == target:
                res.append(list(arr))
                return
            if cur_sum > target or i >= len(candidates):
                return
            
            arr.append(candidates[i])
            dfs(i+1, arr, cur_sum + candidates[i])
            arr.pop()

            next_idx = i + 1
            while next_idx < len(candidates) and candidates[next_idx] == candidates[i]:
                next_idx += 1
            
            dfs(next_idx, arr, cur_sum)
        
        dfs(0, [], 0)
        return res