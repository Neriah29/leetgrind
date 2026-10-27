class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        res = 0
        visited = set()
        def bfs(node):
            visited.add(node)
            queue = deque([node])

            while queue:
                cur = queue.popleft()
                for nbr in graph[cur]:
                    if nbr not in visited:
                        visited.add(nbr)
                        queue.append(nbr)
                
        
        for node in range(n):
            if node not in visited:
                res += 1
                bfs(node)
        
        return res