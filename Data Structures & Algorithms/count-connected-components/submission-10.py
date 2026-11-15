from collections import defaultdict, deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """ 
        union find
        dfs
        bfs
        all solutions in 20 mins 
        """
        #bfs
        visited = set()
        g = defaultdict(set)
        for u,v in edges:
            g[u].add(v)
            g[v].add(u)

        def bfs(node):
            queue = deque([node])
            visited.add(node)

            while queue:
                cur_node = queue.popleft()
                for nbr in g[cur_node]:
                    if nbr not in visited:
                        queue.append(nbr)
                        visited.add(nbr)

            
        res = 0
        for node in range(n):
            if node not in visited:
                bfs(node)
                res += 1
        
        return res