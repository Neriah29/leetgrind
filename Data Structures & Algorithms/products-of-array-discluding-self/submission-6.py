class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        we are going to try and solve this using two passes
        forward and backwards. 
        initialize an array of size len(nums)
        iterate through (forwards and backwards)
        """

        res = [1] * len(nums)
        mult = 1
        #iteration from left to right

        #[1, 2, 4, 6]
        #[1, 1, 2, 8]
        #[1, 24, 12, 8]
        for i in range(1, len(nums)):
            mult *= nums[i-1]
            res[i] *= mult

        mult = 1
        for i in range(len(nums)-2,-1,-1):
            mult *= nums[i+1]
            res[i] *= mult
        
        return res