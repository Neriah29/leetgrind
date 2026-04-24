class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        n = 0  --> [""]
        n = 1  --> ["()"]
        n = 2  --> ["(())", "()()"]
        n = 3  --> ["((()))", "()()()", "(()())", "(())()", "()(())"]
        so you can either add it at the end, around, 
        """
        
        res = []

        def dfs(sub, l, r):
            if l >= n and r >= n:
                res.append(sub)
                return
            
            if l < n:
                dfs(sub+"(", l+1, r)

            if r < l:
                dfs(sub + ")", l, r+1)            

        dfs("(", 1, 0)
        return res