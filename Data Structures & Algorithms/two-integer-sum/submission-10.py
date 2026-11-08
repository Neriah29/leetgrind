class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem = {}
        for idx in range(len(nums)):
            diff = target - nums[idx]
            if diff in rem:
                return[rem[diff], idx]
            rem[nums[idx]] = idx
