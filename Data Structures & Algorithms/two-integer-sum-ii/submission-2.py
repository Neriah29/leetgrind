class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        left and right pointers 
        one starts at the beginning the right at the end, oer iteration do sun 
        if cursum is higher than target, or vicevrsa move pointer in right 
        direction. 
        """

        l, r = 0, len(numbers) - 1 
        while l < r:
            cursum = numbers[l] + numbers[r]

            if cursum > target:
                r -= 1
            elif cursum < target:
                l += 1
            else:
                return [numbers[l], numbers[r]]