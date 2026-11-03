from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        res = []
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        def bfs(row, col, ocean):
            queue = deque([(row, col)])
            ocean.add((row, col))

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS) and (nr, nc) not in ocean and heights[nr][nc] >=heights[r][c]:
                        ocean.add((nr,nc))
                        queue.append((nr, nc))

        for row in range(ROWS):
            bfs(row, 0, pacific)
            bfs(row, COLS-1, atlantic)
        
        for col in range(COLS):
            bfs(0, col, pacific)
            bfs(ROWS-1, col, atlantic)
        
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append([row, col])
        return res