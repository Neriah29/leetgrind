class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#Approach
#iterate over the string and keep a set of things we have seen
#we will have a right and left pointer 
#the right pointer would iterate over the string normally 

        #create set
        seen = set()
        maxNo = 0
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maxNo = max(maxNo, len(seen))
            
        return maxNo