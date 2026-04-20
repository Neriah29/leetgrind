class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        having a window
        left and right pointers
        counter map with the frequency of characters in initial substring 
        counter map with frrequency of characters in window
        O(n)
        we also have to handle cases where it character frequencies are greater.
        """ 

        res = ""
        substringMap = Counter(t)
        windowMap = defaultdict(int)
        valid = set()
        window = None
        flag = True
        d = float("inf")

        #iterate over the string
        #will have left and right pointers showing the window
        l = 0
        
        for r in range(len(s)):
            if flag: l = r
            if s[r] in substringMap:
                flag = False
                windowMap[s[r]] += 1
                if windowMap[s[r]] >= substringMap[s[r]] and s[r] not in valid:
                    valid.add(s[r])
                print(valid)
                while len(valid) >= len(substringMap):
                    if r - l < d: 
                        d =  r- l
                        window = (l,r)
                    print(window)
                    windowMap[s[l]] -= 1
                    if windowMap[s[l]] < substringMap[s[l]]:
                        valid.discard(s[l])
                    l += 1
            

            
        return s[window[0]:window[1]+1] if window else ""
                








