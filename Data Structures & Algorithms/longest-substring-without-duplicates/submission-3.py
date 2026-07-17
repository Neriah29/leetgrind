class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        thinking of using two pointers, once right moves and the 
        '''
        seen = set()
        l = 0
        res = 0
        #for every iteration we want to check if i in seen, till it's not 
        #then we can add s[i] to seen
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, len(seen))
        
        return res


            