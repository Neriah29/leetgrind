class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        we will have an array containing potential maxes, using indexes.
        as r moves, we will increment but if 
        """
        res = []
        maxWindow = deque([])
        l = 0
        for r in range(len(nums)):
            while maxWindow and nums[maxWindow[-1]] < nums[r]:
                maxWindow.pop()
            
            maxWindow.append(r)

            if r - l + 1 < k:
                continue
            res.append(nums[maxWindow[0]])

            if maxWindow[0] == l:
                maxWindow.popleft()
            l += 1

        
        return res
