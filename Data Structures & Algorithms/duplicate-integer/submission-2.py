class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #we are looking for an O(n)
        freq, curr = set(), 0
        for idx in range(len(nums)):
            #nums = [1, 2, 3, 4]
            freq.add(nums[idx])
            if len(freq) <= idx:
                return True
        return False
