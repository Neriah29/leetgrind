class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def dfs(row, col, dist, visited):
            if not(0 <= row < len(grid) and 0 <= col < len(grid[0])) or grid[row][col] == -1 or (dist > 0 and grid[row][col] == 0):
                return

            visited.add((row, col))
            
            if grid[row][col] != 0 and dist >= grid[row][col]:
                return

            for dr, dc in directions:
                if ((row+dr, col+dc)) not in visited:
                    dfs(row + dr, col + dc, dist + 1, visited)

            grid[row][col] = dist

            return 


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    dfs(row, col, 0, set())
        