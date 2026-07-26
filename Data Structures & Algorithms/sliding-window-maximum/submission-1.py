class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        we use a maxHeap for each active window.
        on each iteration, you pop the max. If the index of the max is less than 
        l, keep popping and dont add to res list. 
        """

        #what do we need initialized?
        maxHeap = []
        l = 0
        res= []
        nums = [[-num, idx] for idx, num in enumerate(nums)]

        for r in range(len(nums)):
            heapq.heappush(maxHeap, nums[r])
            if r - l + 1 < k:
                continue
            else:
                while maxHeap[0][1] < l:
                    heapq.heappop(maxHeap)
                res.append(-maxHeap[0][0])
                l+=1
        
        return res

