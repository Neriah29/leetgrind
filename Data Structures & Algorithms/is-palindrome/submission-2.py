class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""
        for letter in s:
            if letter.isalnum():
                if letter.isupper():
                    newString += letter.lower()
                else:
                    newString += letter
            
        rev = newString[::-1]
        print(rev, newString)
        return rev == newString