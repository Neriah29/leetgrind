class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Approach:
        #we will use two pointers, one at index 0, the other at len -1
        #at any point, the integer at the index that is lower has its
        #max possible area

        #initialize l and r
        l, r = 0, len(heights) -1 
        maxArea = -float("inf")
        while l < r:
            d = r - l
            h = min(heights[l], heights[r])
            maxArea = max(maxArea, d * h)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea