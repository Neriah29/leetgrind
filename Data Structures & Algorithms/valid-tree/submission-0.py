from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        a valid tree is acyclic 
        I am thinking of creating an adjacency dictionary
        """
        if len(edges) != n -1:
            return False
        
        graph = defaultdict(set)
        for node, other in edges:
            graph[node].add(other)
            graph[other].add(node)

        visited = set()
        queue = deque([(0,-1)])
        visited.add(0)
        while queue:
            cur, parent = queue.popleft()
            for nbr in graph[cur]:
                if nbr == parent:
                    continue
                elif nbr in visited:
                    return False
                visited.add(nbr)
                queue.append((nbr, cur))
            
        return len(visited) == n