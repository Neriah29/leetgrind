from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        more of bfs
        """
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    grid[row][col] = 0
                    queue.append((row,col))
        time = 0
        directions = [(0,1), (-1,0), (0,-1), (1,0)]
        while queue:
            print(queue)
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    print(nr, nc)
                    if (0 <= nr < ROWS and 0 <= nc < COLS) and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        queue.append((nr, nc))
            time += 1
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] != 0:
                    return -1
        return max(time-1, 0)

        
