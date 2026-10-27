class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        res = 0
        visited = set()

        def dfs(node, par):
            visited.add(node)

            for nbr in graph[node]:
                if nbr not in visited:
                    dfs(nbr, node)

        
        for node in range(n):
            if node not in visited:
                res += 1
                dfs(node, -1)
        
        return res