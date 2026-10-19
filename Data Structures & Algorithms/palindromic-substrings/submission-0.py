class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def palis(l, r):
            if l < 0 or r >= len(s) or (s[l] != s[r]):
                return 0
            return 1 + palis(l-1, r+ 1)
        

        for w in range(len(s)):
            res += palis(w, w) + palis(w, w+1)

        return res