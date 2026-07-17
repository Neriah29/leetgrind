class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        we will use left and right pointers
        since we will always use the minimum, move in the direction of the higher one closer
        to the center
        '''

        l, r = 0, len(heights) -1
        area = 0
        while l < r:
            print (l,r)
            length = min(heights[l], heights[r])
            area = max((length * (r-l)), area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return area