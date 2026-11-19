import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        build my adjacency list

        perform dijkstras
        """ 
        adj = defaultdict(list)

        for u, v, w in times:
            adj[u].append((v,w))

        visited = set()
        time_from_k = {i : float("inf") for i in range(n+1)}
        time_from_k[k] = 0
        heap = [(0,k)]
        
        while heap:
            time, cur = heapq.heappop(heap)
            visited.add(cur)
            if len(visited) == n:
                return time

            for nbr, nbr_time in adj[cur]:
                # print(heap, time_from_k,nbr, visited)
                new_time = time + nbr_time
                if new_time >= time_from_k[nbr]:
                    continue
                time_from_k[nbr] = new_time
                heapq.heappush(heap, (new_time, nbr))


        
        return -1
                



