class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #we are looking for an O(n)
        freq, curr = set(), 0
        for idx in range(len(nums)):
            freq.add(nums[idx])
            if len(freq) <= curr:
                return True
            curr = len(freq)
        return False
