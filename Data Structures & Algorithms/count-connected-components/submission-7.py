class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        union find 
        """
        par = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            cur = node
            while cur != par[cur]:
                par[cur] = par[par[cur]] #should work with or without this
                cur = par[cur]
            return cur #par(cur) should work here as well

        def union(u,v):
            par_u, par_v = find(u), find(v)
            
            if par_u == par_v:
                return 0
            if rank[par_u] > rank[par_v]:
                par[par_v] = par_u
                return 1
            else:
                par[par_u] = par_v
                return 1
        res = n
        for u, v in edges:
            res -= union(u,v)
        return res
                
