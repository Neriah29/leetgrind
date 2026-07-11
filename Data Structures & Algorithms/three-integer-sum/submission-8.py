class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        have a left, middle and right pointer 
        the left moves, and then we do the two sum for the other two 
        """
        res = []
        nums.sort()

        for l in range(len(nums)):
            if l and nums[l] == nums[l-1]:
                continue
            m, r = l+1, len(nums)-1 
            target = -nums[l]

            while m < r:
                cursum = nums[m] + nums[r]
                if cursum > target:
                    r -= 1
                elif cursum < target:
                    m += 1
                else: 
                    res.append([nums[l], nums[m], nums[r]])
                    m += 1
                    while nums[m] == nums[m-1] and m < r:
                        m += 1

        return res
