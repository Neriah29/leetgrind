class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        dfs for all os connected to the edge of the board 
        iterate again and change all os to xs
        """

        not_captured = set()
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        def dfs(r, c):
            if not (0 <= r < len(board) and 0 <= c < len(board[0])) or board[r][c] != "O" or (r,c) in not_captured:
                return 
            not_captured.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)


            
        for row in range(len(board)):
            if board[row][0] == "O":
                dfs(row, col)
            if board[row][-1] == "O":
                dfs(row, col)
        
        for col in range(len(board[0])):
            if board[0][col] == "O":
                dfs(row, col)
            if board[-1][col] == "O":
                dfs(row, col)


        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O" and (row, col) not in not_captured:
                    board[row][col] = "X"