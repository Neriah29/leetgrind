class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        what is the difference between this and the normal combination sum?
        
        at each point, cant go down that path.

        for sure have to sort, 
        """
        candidates.sort()

        
        res = []
        def dfs(i, array, cur_sum):
            # base case:
            if cur_sum == target:
                res.append(list(array))
                return
            if cur_sum > target or i >= len(candidates):
                return

            array.append(candidates[i])
            dfs(i+1, array, cur_sum + candidates[i])
            array.pop()

            next_idx = i+1
            while next_idx < len(candidates) and candidates[i] == candidates[next_idx]:
                next_idx += 1

            dfs(next_idx, array, cur_sum)
        
        dfs(0, [], 0)
        return res

