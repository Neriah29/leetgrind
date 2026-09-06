class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        thoughts:
        we have m and we check is m > or < than the far right index?
        then we also check is target < 
        [3,4,5,6,1,2]
        [6,1,2,3,4,5]
        """

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) //2
            if nums[m] == target:
                return m
            if nums[m] > nums[r]:
                if target <= nums[r] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
                    
                    
        return -1

        