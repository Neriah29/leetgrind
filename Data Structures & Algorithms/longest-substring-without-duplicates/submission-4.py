class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        for this solution i am thinking of a sliding window. 
        with the right pointer being in a for loop and the left moving when a duplicate is introduced
        O(n) space and time would be my guess right now 

        example
        "z x y z x y z"
           ^       ^
        """
        window = set()
        l = 0
        longest = 0
        

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1

            curSize = r - l + 1

            window.add(s[r])
            longest = max(longest, curSize)
        return longest



