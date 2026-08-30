class Solution:
    def trap(self, height: List[int]) -> int:
        """
        we are going to try and get the amount of water on each index. 
        we get that by finding the min of the max(left) and max(right)
        at each index. Sum all that up 
        """

        #create the maximums for left and right map and initialize
        max_left_right ={i : [0,0] for i in range(len(height))} #O(n)

        #so now every index maps to [0,0]
        #we will iterate from left to right then right to left in two different passes

        #right sweepm -> gives us the max on the left
        cur_max = 0
        for idx in range(1, len(height)): #O(n)
            cur_max = max(cur_max, height[idx-1])
            #now i can update the left pointer of each index in the map
            max_left_right[idx][0] = cur_max

        cur_max = 0
        #left sweep -> right max
        for idx in range(len(height)-2, -1, -1):
            cur_max = max(cur_max, height[idx+1])
            #now i can update the left pointer of each index in the map
            max_left_right[idx][1] = cur_max
        
        #now we have the max from the left and right we can iterate over each index and figure out 
        #how much water is actually there.
        total_water = 0
        for idx in range(len(height)):
            h = min(max_left_right[idx])
            cur_water = max(0, h - height[idx])
            total_water+= cur_water
            
        
        return total_water


