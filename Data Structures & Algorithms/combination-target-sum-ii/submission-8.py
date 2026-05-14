class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        res = set()

        def dfs(i, cur, sub):
            if cur == target:
                res.add(tuple(sub))
                return
            
            if i >= len(candidates) or cur > target:
                return 
            
            sub.append(candidates[i])
            dfs(i+1, cur + candidates[i], sub)

            sub.pop()
            dfs(i+1, cur, sub)
        
        dfs(0,0,[])
        return [list(tpl) for tpl in res]

