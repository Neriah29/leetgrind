class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        the idea is to try and remove all non alphanum characters in the string first
        after that, place them in an array. 
        then, if odd number, begin from the dead center. else if even, l and r point at the 
        two middle, then do the recursion outwards from there
        """

        def ispalindrome(array):
            length = len(array)
            if len(array) % 2:
                #if odd, we want the l and r to start from the dead center = len(sentence) // 2
                l = r = length // 2
            else:
                l, r = (length // 2) - 1, (length // 2)

            while l > -1 and r < length:
                if array[l] == array[r]:
                    l -= 1
                    r += 1
                else:
                    return False
            return True

        sentenceArray = []

        for i in range(len(s)):
            #iterate over each character
            if s[i].isalnum():
                #if the character is alphanumeric, add it to sentence in lowercase
                sentenceArray.append(s[i].lower())
        
        return ispalindrome(sentenceArray)

            