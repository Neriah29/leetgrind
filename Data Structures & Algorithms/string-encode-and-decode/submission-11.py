class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        we cant use strings or numbers here, because we cant assume the input wouldnt have 
        that. So we try doing this mathematically
        for every element in the list, 
        """
        #initialize the string
        string = ""

        #loop over all the elements int he str array and add the number to the beginning
        for s in strs:
            string += str(len(s)) + "#" + s
        return string
        #eg 5#hello5#world
        
    def decode(self, s: str) -> List[str]:
        """
        here, we will try and iterate over the string returned and check till we get a hash
        then we pause there then go the 
        """
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            stringLength = int(s[i:j])
            res.append(s[j+1: j+1+stringLength])
            i = j + 1 + stringLength
        return res

