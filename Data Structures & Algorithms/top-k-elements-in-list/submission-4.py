class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        we are dealing with frequency
        possibly use counter? then items and make a heap based on that and keep popping 
        until we have k 

        time complexity = O(nlog(n) or k log(n))
        space = O(n)

        can we do better?

        use counter, create a list of lists up to n
        unpack with items and then append accordingly until x is reachee
        bucket sort
        """ 
        
        freqPairs = [[] for i in range(len(nums)+1)]
        freqMap = Counter(nums)
        res = []

        for num, freq in freqMap.items():
            freqPairs[freq].append(num)

        
        for i in range(len(freqPairs) -1, -1, -1 ):
            for num in freqPairs[i]:
                res.append(num)
                if len(res) >= k: return res

