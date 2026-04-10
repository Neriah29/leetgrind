class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numPair = [(num, idx) for idx, num in enumerate(nums)]
        numPair.sort()
        l, r = 0, len(nums) -1
        while l <= r:
            curr = numPair[l][0] + numPair[r][0]
            if curr > target:
                r -= 1
            elif curr < target:
                l += 1
            else:
                return sorted([numPair[l][1], numPair[r][1]])