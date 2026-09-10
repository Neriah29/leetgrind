class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        without using space and modifying the array, 
        [1, 2, 3, 2, 2]
        """
        #negative marking
        for idx in range(len(nums)):
            num_idx = abs(nums[idx]) - 1
            if nums[num_idx] < 0:
                return num_idx + 1
            nums[num_idx] *= -1


