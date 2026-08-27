class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        my thoughts:
        creating a set 
        then iterating through the array and checking if any value 1 below it is in the array
        if so, then continue. Once you find the least, start counting the max. We avoid ever
        counting an element twice
        """

        check = set(nums)
        longest = 0
        for num in nums:
            if num - 1 in check:
                continue
            curLongest = 0
            cur = num
            while cur in check:
                curLongest += 1
                longest = max(longest, curLongest)
                cur += 1
            
        return longest
