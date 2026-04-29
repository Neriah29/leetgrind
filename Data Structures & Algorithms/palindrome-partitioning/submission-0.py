class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def dfs(i, part):
            print(i)
            if i>=len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                cur = s[i:j+1]
                if self.ispali(cur):
                    print(part)
                    part.append(cur)
                    dfs(j+1, part)
                    part.pop()
        dfs(0,[])
        return res
    
    def ispali(self, word):
        pass
        if len(word) < 2:
            return True
        if word[0] == word[-1]:
            return self.ispali(word[1:-1])
        else:
            return False
        
        