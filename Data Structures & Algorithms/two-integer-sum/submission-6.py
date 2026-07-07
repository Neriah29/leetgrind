class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numPair = [(val, idx) for idx, val in enumerate(nums)]

        numPair.sort()

        l, r = 0, len(nums) -1
        while l < r:
            cur = numPair[l][0] + numPair[r][0]
            print (cur)
            if cur > target:
                r -= 1
            elif cur < target:
                l += 1
            else:
                print(l, r)
                return sorted([numPair[l][1], numPair[r][1]])


        