class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        what is the difference between this and the normal combination sum?
        
        at each point, cant go down that path.

        for sure have to sort, 
        """
        candidates.sort()

        
        res = set()
        def dfs(i, array, cur_sum):
            # base case:
            if cur_sum == target:
                res.add(tuple(array))
                return
            
            if cur_sum > target:
                return
            if i >= len(candidates):
                return
            array.append(candidates[i])
            dfs(i+1, array, cur_sum + candidates[i])
            array.pop()
            dfs(i+1, array, cur_sum)
        
        dfs(0, [], 0)
        return [list(tpl) for tpl in res]

