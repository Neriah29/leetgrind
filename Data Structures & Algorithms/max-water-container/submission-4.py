class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        thoughts:
        two pointer, starting at both extremes then slim it down over time. At every point, 
        whichever is pointer is at where is less is where we will move at that iteration 


        [1,3,4,5,6,7]
         ^         ^
        [1,3,4,5,6,7]
           ^       ^
        """

        l, r = 0, len(heights) -1
        maxArea = -float("inf")

        while l < r:
            width = r - l
            length = min(heights[l], heights[r])
            area = width * length

            if heights[l] < heights[r]:
                l += 1
            else: 
                r -= 1
            maxArea = max(area, maxArea)
        
        return maxArea

