class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        plan:
        make it a set, if not first part of sequence skip
        to next for loop 

        way of thinking:
        look for a characteristic of a consecutive sequence. 
        WE know that there will always be a minimum number out of the sequence
        so we are always certain that if we make conditions for the minimum num
        there, then an error result of 0 is alr covered. 
        """


        #make the set containing all distinct numbers

        numSet = set(nums)
        res = 0

        for num in nums:
            if num - 1 in numSet:
                continue 
            count = 1
            cur = num
            while num + 1 in numSet:
                count += 1
                num += 1
            res = max(res, count)

        return res