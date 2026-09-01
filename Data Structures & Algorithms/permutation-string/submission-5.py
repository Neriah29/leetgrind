class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Sliding Window (fixed size of len(s1))
        Use a "count" hashmap to count the frequency of the characters. 
        For every loop, check if that is the permutation
        """

        #hashmap for the original string 
        originalCounter = {}
        for i in range(len(s1)):
            originalCounter[s1[i]] = originalCounter.get(s1[i], 0) + 1

        secondCounter = {}
        l = 0
        ValidCharacters = set()

        for r in range(len(s2)):
            #on every iteration, we want to add then check if everything is perfect
            #ad the r to the window
            secondCounter[s2[r]] = secondCounter.get(s2[r], 0) + 1

            if r - l + 1 > len(s1):
                secondCounter[s2[l]] -= 1
                ValidCharacters.discard(s2[l])
                l += 1
            
            if s2[r] in originalCounter and secondCounter[s2[r]] == originalCounter[s2[r]]:
                ValidCharacters.add(s2[r])
            if len(ValidCharacters) == len(originalCounter):
                return True
            print(originalCounter, secondCounter, ValidCharacters)
        
        return False

            

            

