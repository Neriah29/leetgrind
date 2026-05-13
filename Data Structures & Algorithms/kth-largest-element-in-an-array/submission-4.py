class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nsmallest(len(nums)-k+1, nums)[-1]