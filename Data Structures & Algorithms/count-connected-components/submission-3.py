from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        def dfs(node):
            visited.add(node)
            
            for nbr in graph[node]:
                if nbr not in visited:
                    visited.add(nbr)
                    dfs(nbr)
        
        res = 0
        for node in range(n):
            if node not in visited:
                res += 1
                dfs(node)
        
        return res