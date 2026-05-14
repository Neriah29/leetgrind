class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        prioritize frequency 
        what determines what comes next?
        frequency and is it valid? Remove from available pool if invalid
        """


        time = 0
        count = Counter(tasks)
        maxHeap = [-val for val in count.values()]
        heapq.heapify(maxHeap)
        q = deque([])

        while maxHeap or q:
            time += 1
            if maxHeap:
                currTask = heapq.heappop(maxHeap)
                if currTask < -1:
                    q.append((currTask +1, time+n))
            
            if q and q[0][1] <= time:
                heapq.heappush(maxHeap, q.popleft()[0])
            
        return time
