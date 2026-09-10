class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        without using space and modifying the array, 
        [1, 2, 3, 2, 2]
        """
        #negative marking
        for num in nums:
            idx = num - 1
            if nums[idx] < 0:
                return num
            nums[idx] *= -1
            
