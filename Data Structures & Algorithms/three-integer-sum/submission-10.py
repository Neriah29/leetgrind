class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        sort through the list O(nlogn)
        then run through the two sum solution
        """
        res = []
        nums.sort()

        for i in range(len(nums)):
            """
            we are trying to iterate over each element in the array and then run a two sum solution for   
            each index  
            """
            if i and nums[i] == nums[i-1] :
                continue

            target = -nums[i]
            l, r = i + 1, len(nums) -1

            while l < r: 
                cur = nums[l] + nums[r]
                if cur < target:
                    l += 1
                elif cur > target:
                    r -= 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    
                    #we have now found an appropriate solution, we want to make sure that the next l 
                    #is different from what we have already appended
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res
                
