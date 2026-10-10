class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        dfs wherever there is a 1.
        """
        def dfs(row, col):
            if grid[row][col] != "1":
                return
            
            grid[row][col] = 0
            
            if row > 0:
                dfs(row-1,col)
            if row < len(grid)-1:
                dfs(row+1, col)
            if col > 0:
                dfs(row, col -1 )
            if col < len(grid[0]) -1:
                dfs(row, col + 1)

        

        num = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    num += 1
                    dfs(row, col)

        return num