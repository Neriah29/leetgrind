class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        it is already sorted
        this seems to be the normal two sum
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            left, right = numbers[l], numbers[r]
            rem = target - left

            if right > rem:
                r -= 1
            elif right < rem:
                l += 1
            else:
                return [l + 1, r + 1]
            
            

        