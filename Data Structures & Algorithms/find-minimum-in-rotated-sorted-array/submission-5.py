class Solution:
    def findMin(self, nums: List[int]) -> int:

#initalise left and right pointer
#game plan is that my lower bound eventually points to the minimum

        l, r = 0, len(nums)-1
        while l < r:
            m = (l+r)//2

            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m
        
        return nums[l]