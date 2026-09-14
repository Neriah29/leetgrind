class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        I am thinking that we will try iterating over the list and making
        that index negative. That way, we can notice that if that point is now 
        negative, it had been gone over before
        """


        for num in nums:
            if nums[abs(num)] < 0:
                return abs(num)
            nums[abs(num)] = -nums[abs(num)]
        

