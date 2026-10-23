class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        dfs
        """
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        def dfs(row, col):


            if not(0<= row < len(grid) and 0<= col < len(grid[0])) or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0
            res = 0
            for dr, dc in directions:
                res += dfs(row+dr, col+dc)
            return res + 1


        area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    cur = dfs(row, col)
                    area = max(cur, area)
        
        return area