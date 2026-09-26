class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        thoughts:
        prioritize higher freq, as far as valid

        space -> O(1) --> counter for alph -> 26

        maxheap of tasks
        queue of tasks in waiting.
        once off waiting, back to maxheap. 
        ie if in maxheap, valid 
        """

        # we will have a counter of the tasks, frequency 
        task_frequency = {}
        for task in tasks:
            task_frequency[task] = 1 + task_frequency.get(task, 0)

        maxheap = [-freq for taks, freq in task_frequency.items()]
        heapq.heapify(maxheap)

        invalid = deque()
        cycle = 0 
        while maxheap or invalid:
            if maxheap: 
                cur_max = heapq.heappop(maxheap)
                if cur_max < -1:
                    invalid.append([cur_max + 1, cycle + n])
            
            if invalid and invalid[0][1] <= cycle:
                now_valid_task = invalid.popleft()
                heapq.heappush(maxheap, now_valid_task[0])


            cycle += 1

        return cycle
