class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        prioritize frequency off rip
        keep track of the count of each letter and the cooldown remaining.
        queue = contain the cooldown and remaining count
        ["A","A","A","B","C"]
        heap = [-3, -1, -1] heappop = [-1, -1] queue = [(-3+1, n + time)]
        """

        #we need to initialise the maxheap with the values of frequency
        countMap = {}
        queue, time = deque([]),0
        curr = None
        for i in tasks:
            countMap[i] = countMap.get(i, 0) + 1    
        maxHeap = [-x for x in countMap.values()]
        heapq.heapify(maxHeap)

        while maxHeap or queue:
            time += 1
            if maxHeap:
                curr = heapq.heappop(maxHeap) 
                if curr < -1:
                    queue.append((curr+1, n + time))

            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
            print(maxHeap, list(queue), time)
            
        return time