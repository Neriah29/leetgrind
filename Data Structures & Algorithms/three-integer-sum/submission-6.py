class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for l in range(len(nums)):
            if l and nums[l-1] == nums[l]:
                continue
            m = l + 1
            r = len(nums)-1 
            target = - nums[l]

            while m < r:
                curr = nums[m] + nums[r]
                if curr > target:
                    r -= 1
                elif curr < target:
                    m += 1
                else:
                    res.append([nums[l], nums[m], nums[r]])
                    m += 1

                    while nums[m] == nums[m-1] and m < r:
                        m += 1
        
        return res

