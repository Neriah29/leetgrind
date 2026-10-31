class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        union find
        """
        par =[i for i in range(n)]
        rank = [0 for _ in range(n)]

        def find(node):
            cur = par[node]
            while cur != par[cur]:
                par[cur] = par[par[cur]]
                cur = par[cur]
            return cur
        
        def union(u, v):
            p1, p2 = find(u), find(v)

            if p1 == p2:
                return 0

            elif rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += 1 
            else:
                par[p1] = p2
                rank[p2] += 1
            return 1
        
        res = n
        for u, v in edges:
            res -= union(u,v)
        return res

            