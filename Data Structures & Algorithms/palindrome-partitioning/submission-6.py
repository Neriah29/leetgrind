class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispali(w):
            if len(w) < 2:
                return True 
            if w[-1] == w[0]:
                return ispali(w[1:-1])
            else:    
                return False
        
        res = []
        def dfs(i, cur):
            if i >= len(s):
                res.append(cur.copy())
                return 
            
            for j in range(i, len(s)):  
                sub = s[i:j+1]
                if ispali(sub):
                    cur.append(sub)
                    dfs(j+1, cur)
                    cur.pop()
        
        dfs(0, [])
        return res