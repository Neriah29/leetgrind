"""
we will have a fast and slow pointer 
eventually we know the fast and slow pointer will intersect
from the point they intersect and with a slow pointer at the 
beginning, where they meet will be the beginning of the loop
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                break 
        
        return slow

        