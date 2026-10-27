class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        visited = set()
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(cur, par):
            visited.add(cur)

            for nbr in graph[cur]:
                if nbr == par:
                    continue 
                if nbr in visited:
                    return False
                if not dfs(nbr, cur):
                    return False
            
            return True 
        
        if not dfs(0,-1):
            return False
        return len(visited) == n