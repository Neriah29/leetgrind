class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #sort the list 0(n)
        #edge case:
        #if nums.length is 0 or 1, return the nums.length
        #initialize currCount and maxCount to be 0
        #iterate over the sorted list
        #if curr index is prev index + 1, increment currCount
        #maxcount = max(maxCount, currCount)
        #return maxcount.

        if not len(nums) or len(nums) == 1:
            return len(nums)

        nums.sort()
        currCount, maxCount = 0, 0

        for i in range(len(nums)):
            if not i:
                currCount = 1
            elif nums[i] == nums[i-1] + 1:
                currCount += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                currCount = 1
            
            maxCount = max(maxCount, currCount)
        
        return maxCount


