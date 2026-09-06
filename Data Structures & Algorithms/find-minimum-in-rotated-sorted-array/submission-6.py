class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        my thoughts
        we still use binary search 
        if m 
        [4,0,1,2,3]
        [3,4,5,6,1,2]

        compare the middle with the far right
        """

        l, r = 0, len(nums)- 1
        while l < r:
            m = (r + l) // 2

            if nums[m] > nums[r]:
                l = m + 1
            
            else:
                r = m
        
        return nums[l]
