class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        check = set()
        for idx in range(len(nums)):
            check.add(nums[idx])
            if len(check) != idx+1:
                return nums[idx]
