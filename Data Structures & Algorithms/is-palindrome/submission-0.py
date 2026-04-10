class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal_string = []
        for string in s:
            if string.isalnum():
                pal_string.append(string.lower())
        if pal_string == pal_string[::-1]:
            return True
        return False
