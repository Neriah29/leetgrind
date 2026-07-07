class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        top X frequent.
        Thoughts:
        use counter to keep track of the frequency of all integers (O(n))

        use heapify to deal with the sorting.  O(n)
        Loop for K times, popping and returning that K log (n)
        """

        count = Counter(nums)
        
        #we are tring to retrieve the actual frequencies and reverse heap those

        maxHeap = [(-numFrequency, num) for num, numFrequency in count.items()]

        heapq.heapify(maxHeap)

        #we now have the frequencies sorted in reverse(from max to min. we loop
        #popping the most frequent K times
        #we are looking for the second index in numpar
        res = []
        for i in range(k):
            cur = heapq.heappop(maxHeap)
            res.append(cur[1])
        
        return res
