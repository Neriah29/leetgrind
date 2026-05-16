class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(l, r, s):
            if l == n and r == n:
                res.append(s)
                return
            
            if l < n:
                dfs(l+1,r,s+"(")
            if r < l:
                dfs(l,r+1,s+")")
        
        dfs(1,0,"(")
        return res
