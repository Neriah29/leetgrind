class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        we are trying to return where we found the first cycle
        brute force:
        as building out the graph, try dfsing. First with a cycle is intruder

        union find, if I am joining two diff and the parentsa re alr the same, cycle
        """

        n = len(edges)+1
        par = [i for i in range(n)]
        rank = [0 for i in range(n)]

        def find(node):
            cur_node = node
            while cur_node != par[cur_node]:
                par[cur_node] = par[par[cur_node]]
                cur_node = par[cur_node]
            return cur_node
        
        def union(n1, n2):
            par1, par2 = find(n1), find(n2)
            if par1 == par2:
                return False
            if rank[par1] > rank[par2]:
                par[par2] = par1
                rank[par1] += 1
            else:
                par[par1] = par2
                rank[par2] += 1
            return True 
        
        for u,v in edges:
            if not union(u, v):
                return [u,v]

