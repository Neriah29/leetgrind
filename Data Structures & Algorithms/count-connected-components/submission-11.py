class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        union-find
        """
        par = [i for i in range(n)]
        rank = [0 for i in range(n)]

        def find(node):
            cur = node
            while cur != par[cur]:
                par[cur] = par[par[cur]]
                cur = par[cur]
            return cur

        def union(node1, node2):
            par1, par2 = find(node1), find(node2)

            if par1 == par2:
                return 0
            if rank[par1] > rank[par2]:
                par[par2] = par[par2]
            else:
                par[par1] = par[par2]
            
            return 1
        res = n   
        for u,v in edges:
            res -= union(u,v)  
        return res
