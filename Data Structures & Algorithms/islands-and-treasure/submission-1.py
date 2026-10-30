from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Graph search 
        The issue wit doing a DFS here is that 
        Multi-Source BFS

        i need all the treasures, first to hit land, use the dist of callee + 1
        """
        INF  = (2**31) - 1
        ROWS, COLS = len(grid), len(grid[0])

        queue = deque()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row, col))

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS) and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))  

