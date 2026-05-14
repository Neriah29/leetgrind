class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        count = Counter(candidates)
        candidates= set(candidates)
        candidates = sorted(candidates)
        res =  []

        def dfs(i, cur, sub):
            if cur == target:
                res.append(sub.copy())
                return
            
            if i >= len(candidates) or cur > target:
                return 


            if count[candidates[i]] > 1:
                for x in range(count[candidates[i]]):
                    dfs(i+1, cur + (x+1)*candidates[i], sub + [candidates[i]] * (x+1))
                dfs(i+1, cur, sub)
                

            else:
                sub.append(candidates[i])
                dfs(i+1, cur + candidates[i], sub)

                sub.pop()
                dfs(i+1, cur, sub)

        
        dfs(0,0,[])
        return res

