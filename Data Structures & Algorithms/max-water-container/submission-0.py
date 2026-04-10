class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0 
        if len(heights) < 2:
            return 0
        for idx in range(len(heights)-1):
            for idx2 in range(idx+1, len(heights)):
                if heights[idx] > heights[idx2]:
                    height = heights[idx2]
                else:
                    height = heights[idx]
                area = height * (idx2 - idx)
                if area > max_area:
                    max_area = area

        return max_area