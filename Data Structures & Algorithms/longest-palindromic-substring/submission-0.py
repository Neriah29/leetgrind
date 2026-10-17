class Solution:
    def longestPalindrome(self, s: str) -> str:
        """

        """
        res = 0
        window  = [0,0]
        def pali(l,r):
            if l < 0 or r >= len(s) or (s[l] != s[r]):
                return (l + 1, r - 1) 
            if s[l] == s[r]:
                return pali(l-1, r + 1)

        for i in range(len(s)):
            a = pali(i,i)
            b = pali(i, i+1)
            if a[1] - a[0] > window [1] - window[0]:
                window = a
            if b[1] - b[0] > window [1] - window[0]:
                window = b
            

        return s[window[0]:window[1]+1]
            

