class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for l in range(len(nums)):
            if nums[l] == nums[l-1] and l > 0:
                continue
            m, r = l+1, len(nums) -1
            newTarget = -nums[l]

            while m < r:
                total = nums[m] + nums[r]
                if total > newTarget:
                    r -= 1
                elif total < newTarget:
                    m += 1
                else:
                    res.append([nums[l], nums[m], nums[r]])
                    m += 1
                    while nums[m] == nums[m-1] and m < r:
                        m += 1
        
        return res





