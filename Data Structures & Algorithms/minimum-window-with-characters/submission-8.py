class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        sliding window approach 
        counter hashmap for original string t

        we slide the window throughout s:
        we check to see if the conditions are satisfied, ie the counts are at least the same 
        as in the original hashmap 

        if condition is ever met, we move the left pointer till condition becomes false
        then continue moving the right and repeat until we reach the end
        """

        #we have the original counter for t 
        tStringCounter = {}
        for idx in range(len(t)):
            curChar = t[idx]
            tStringCounter[curChar] = tStringCounter.get(curChar, 0) + 1

        
        #we move on to the window for s
        #we keep track of the minimumIndexes, validCharacters, left pointer
        minWindow = []
        validCharacters = set()
        sStringCounter = {}
        l = 0

        for r in range(len(s)):
            #we add the r index to the window, if it is relevant
            curChar = s[r]
            if curChar in tStringCounter: #means it is relevant
                sStringCounter[curChar] = sStringCounter.get(curChar, 0) + 1
                if sStringCounter[curChar] >= tStringCounter[curChar]:
                    validCharacters.add(curChar)

            #first time the condition is met
            if not minWindow and len(validCharacters) == len(tStringCounter) :
                minWindow = [l,r]
            
            while (len(validCharacters) == len(tStringCounter) ):
                if s[l] in tStringCounter:
                    sStringCounter[s[l]] -= 1
                    if (sStringCounter[s[l]] < tStringCounter[s[l]]):
                        validCharacters.discard(s[l])
                l += 1

            if minWindow and r - l + 2 < minWindow[1] - minWindow[0] + 1: 
                minWindow = [l-1, r]
            
        return s[minWindow[0]: minWindow[1] + 1] if minWindow else ""
                

