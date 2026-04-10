class Solution:
    def trap(self, height: List[int]) -> int:
#Approach
#if you notice, at every index, the amount of water blocks
#that can be stored there is 
#min(max(left), max(right)) of that index - the value of that index (if -ve, = 0)

        #create hashmap where the max(left) and right of indexes
        #will be stored/mapped to
        
        #edgecase where result is always going to be 0
        if len(height) < 3:
            return 0

        maxMap = defaultdict(list)
        
        #first, we look for max(left) of each index
        currMax = -float("inf")
        for i in range(1, len(height)-1):
            currMax = max(currMax, height[i - 1])
            maxMap[i].append(currMax)
        #then, we look for max(right) of each index
        currMax = -float("inf")
        for i in range(len(height)-2, 0, -1):
            currMax = max(currMax, height[i + 1])
            maxMap[i].append(currMax)
        res = 0
        for i in range(1, len(height)-1):
            res += max(0, min(maxMap[i]) - height[i])
        return res
