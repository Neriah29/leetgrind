class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        two pointers, r and l
        iterate with r.
        for every r iteration, we check if incoming is less or more. 
        if less, append, if more than [-1] idx then pop that one and move onto the next
        """

        window = deque([])
        res = []

        for r in range(len(nums)):
            while window and nums[r] > nums[window[-1]]:
                window.pop()
            
            window.append(r)
            
            while window[0] <= r - k:
                window.popleft()
            
            if r + 1 >= k:
                res.append(nums[window[0]])
            else:
                continue
        
        return res


            

