class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for i in s:
            if i.isalnum():
                new += i.lower()
            else:
                continue
        print(new)
        rev = new[::-1]
        if rev == new:
            return True
        else:
            return False
            