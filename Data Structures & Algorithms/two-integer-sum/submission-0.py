class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx in range(len(nums)-1):
            for idx2 in range(idx+1, len(nums)):
                if nums[idx] + nums[idx2] == target:
                    return [idx, idx2]