class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def a(l, r):
            m = (l+r)//2
            if l > r:
                return -1
            elif nums[m] == target:
                return m
            elif nums[m] > target:
                return a(l, m-1)
            else:
                return a(m+1,r)
        return a(0, len(nums)-1)