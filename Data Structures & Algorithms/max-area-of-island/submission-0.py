class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        dfs
        """
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        def dfs(row, col, area):

            if not(0<= row < len(grid) and 0<= col < len(grid[0])) or grid[row][col] == 0:
                return area
            
            grid[row][col] = 0
            area += 1
            res = 0
            for dr, dc in directions:
                res = max(dfs(row+dr, col+dc, area), res)

            return res

        area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    cur = dfs(row,col, 0)
                    area = max(cur, area)
        
        return area