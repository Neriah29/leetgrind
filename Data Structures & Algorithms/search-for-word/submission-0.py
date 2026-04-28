class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        thoughts:
        possibly doing a dfs for every position/coordinate
        same thing 

        dfs function

        iterate over every coordinate in the grid
        """
        flag = False
        def dfs(row, col, p):
            nonlocal flag
            if p>= len(word) or board[row][col] != word[p]:
                return
            if p == len(word)-1:
                flag = True
            if row < len(board) - 1:
                dfs(row+1, col, p+1)
            if row > 0:
                dfs(row - 1, col, p+1)
            if col < len(board[row]) - 1:
                dfs(row, col + 1, p+1)
            if col > 0:
                dfs(row, col - 1, p+1)
            print("h")
            

        #iterate over every position. 
        #for every position, we run this dfs 
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    dfs(row,col,0)
        
        return flag
