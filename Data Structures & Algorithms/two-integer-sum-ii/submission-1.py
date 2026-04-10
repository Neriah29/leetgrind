class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #already sorted 
        #have two pointers, one at the first index and another at the end
        #curr = the current sum of both elements at the pointers
        #depending on the value of curr relative to the target
        #we adjust the pointers accordingly
        #until we eventually get the solution as we are told there
        #will always be one

        l, r = 0, len(numbers) -1
        while l< r:
            curr = numbers[l] + numbers[r]
            if curr > target:
                r -= 1
                while numbers[r] == numbers[r+1] and r > l:
                    r -= 1
            elif curr < target:
                l += 1
                while numbers[l] == numbers[l-1] and l < r:
                    l += 1
            else:
                return [l+1, r+1]