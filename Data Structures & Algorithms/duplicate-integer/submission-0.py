from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict1 = defaultdict(int)
        for num in nums:
            dict1[num] += 1
        flag = False
        for key in dict1:
            if dict1[key] != 1:
                flag = True
        return flag
