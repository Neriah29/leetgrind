import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        build out the graph 
        dijkstras 
        """

        graph = defaultdict(list)
        for u, v, time in times:
            graph[u].append((v, time))
        
        time_from_k = {i: float("inf") for i in range(1,n+1)}
        time_from_k[k] = 0

        heap = [(0,k)]
        visited = set()
        while heap:
            time, cur = heapq.heappop(heap)
            visited.add(cur)
            if len(visited) == n:
                return time
            for nbr, time_from_cur in graph[cur]:
                new_time = time + time_from_cur
                if new_time >= time_from_k[nbr]:
                    continue
                time_from_k[nbr] = new_time
                heapq.heappush(heap, (new_time, nbr))
        
        return -1
