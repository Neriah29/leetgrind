class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        dfs in
        corners are fs
        """
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        visited = set()

        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        def dfs(r, c):
            if not(0 <= r < ROWS and 0 <= c < COLS) or (r, c) in visited:
                return
            
            visited.add((r,c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS) and heights[nr][nc] <= heights[r][c]:
                    dfs(nr, nc)
                    if (nr, nc) in pacific:
                        pacific.add((r, c))
                    if (nr, nc) in atlantic:
                        atlantic.add((r,c))

        
        for row in range(ROWS):
            pacific.add((row, 0))
            atlantic.add((row, COLS-1))
        
        for col in range(COLS):
            pacific.add((0, col))
            atlantic.add((ROWS-1, col))
        
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in visited:
                    dfs(row, col)
        res = []
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in pacific and (row,col) in atlantic:
                    res.append([row, col])
        
        return res
                    