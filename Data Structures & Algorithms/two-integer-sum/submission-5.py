class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numPair = [(idx, num) for idx, num in enumerate(nums)]
        numPair.sort(key = lambda x:x[1])
        l, r = 0, len(nums) -1
        while l <= r:
            curr = numPair[l][1] + numPair[r][1]
            if curr > target:
                r -= 1
            elif curr < target:
                l += 1
            else:
                return sorted([numPair[l][0], numPair[r][0]])