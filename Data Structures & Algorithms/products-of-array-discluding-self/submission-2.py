class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count, numsProd = 0, 1
        res = []
        for num in nums:
            if num == 0:
                zero_count += 1
                continue
            else:
                numsProd *= num
            
        #if there is more than one zero in the list then all the figures will be zero.
        if zero_count > 1:
            return [0 for num in nums]
       
        for idx in range(len(nums)):
            if nums[idx] == 0:
                res.append(int(numsProd))
            elif zero_count:
                res.append(0)
            else:  
                res.append(int(numsProd/nums[idx]))

        return res
            
        