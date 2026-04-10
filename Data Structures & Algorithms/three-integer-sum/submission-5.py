class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for l in range(len(nums)-2):
            if l and nums[l] == nums[l-1]:
                continue
            m = l + 1
            r = len(nums)-1
            target = - nums[l]

            while m < r:
                numsum = nums[m] + nums[r]
                if numsum > target:
                    r -= 1
                elif numsum < target:
                    m += 1
                else:
                    res.append([nums[l], nums[m], nums[r]])
                    m += 1
                    while nums[m] == nums[m-1] and m < r:
                        m += 1
                
        return res
