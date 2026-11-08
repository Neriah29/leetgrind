class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        so once we find a cycle, 
        """
        visited = set()
        for u, v in edges:
            if u in visited and v in visited:
                return [u, v]
            else:
                visited.add(u)
                visited.add(v)