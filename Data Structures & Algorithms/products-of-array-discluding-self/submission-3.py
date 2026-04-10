class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #the idea is to have a prefix array contianing the miltuples up until that point
        #[x,x,x,x]
        #the first index of the array is going to be 1.
        #so we can put 1 there as a place holder for everything then assign them new values as we iterate

        prefix = [1 for num in nums]

        #[now there are n 1s in the prefix array]
        #curr is going to stand as the prefix which we will update per iteration step in the array
        curr = 1
        #actually iterate over nums
        for i in range(len(nums)):
            prefix[i] = curr
            #update curr for the next iteration
            curr *= nums[i]
        
        #so at this point, prefix[i] contains the multiplications prior tot he ith index of nums.        
        #do same process for the reverse/postfix
        
        curr = 1
        for i in range(len(nums)-1, -1, -1):
            prefix[i] *= curr
            curr *= nums[i]

        return prefix