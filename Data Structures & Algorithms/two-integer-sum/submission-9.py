class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        trying to get an O(n) solution
        using a hashmap 
        map the cur to its index after checking what i necessary isnt in the hashmap

        """
        Map = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in Map:
                return [Map[needed], i]
            
            Map[nums[i]] = i
        