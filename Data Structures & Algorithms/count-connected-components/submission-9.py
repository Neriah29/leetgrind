from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """ 
        union find
        dfs
        bfs
        all solutions in 20 mins 
        """
        #dfs
        g = defaultdict(set)
        visited = set()

        for u,v in edges:
            g[u].add(v)
            g[v].add(u)


        def dfs(node):
            visited.add(node)

            for nbr in g[node]:
                if nbr not in visited:
                    dfs(nbr)


            pass

        res = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1
        
        return res