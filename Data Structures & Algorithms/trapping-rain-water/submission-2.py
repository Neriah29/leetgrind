class Solution:
    def trap(self, height: List[int]) -> int:
        """
        the area at that index is the 
        """

        maxLeftRight = defaultdict(list)
        #leftpass
        res = 0
        curmax = 0
        for i in range(len(height)):
            maxLeftRight[i].append(curmax)
            curmax = max(curmax, height[i])
        curmax = 0
        for i in range(len(height)-1, -1, -1):
            maxLeftRight[i].append(curmax)
            curmax = max(curmax, height[i])
        
        for i in range(len(height)):
            minmax = min(maxLeftRight[i])
            print(minmax)
            curlevel = max(minmax-height[i], 0)
            res += curlevel
        
        return res
        
