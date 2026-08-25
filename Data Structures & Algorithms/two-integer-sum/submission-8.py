class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numPairs = [(num, idx) for idx, num in enumerate(nums)]
        numPairs.sort()

        l, r = 0, len(nums) - 1
        while l < r:
            leftidx, rightidx = numPairs[l][1], numPairs[r][1]
            print (leftidx, rightidx)
            cur = numPairs[l][0] + numPairs[r][0]

            if cur < target:
                #too small we want to increase l
                l += 1
            
            elif cur > target:
                #too large, we want to reduce r
                r -= 1
            
            else:
                return [min(leftidx,rightidx), max(leftidx,rightidx)]
                 