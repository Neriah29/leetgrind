class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        dfs for all os connected to the edge of the board 
        iterate again and change all os to xs
        """
        ROWS, COLS = len(board), len(board[0])
        not_captured = set()
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        def dfs(r, c):
            if not (0 <= r < len(board) and 0 <= c < len(board[0])) or board[r][c] != "O":
                return 
            if (r,c) in not_captured:
                return
            not_captured.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            return

        for row in range(ROWS):
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][COLS-1] == "O":
                dfs(row, COLS-1)
        
        for col in range(COLS):
            if board[0][col] == "O":
                dfs(0, col)
            if board[ROWS-1][col] == "O":
                dfs(ROWS-1, col)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O" and (row, col) not in not_captured:
                    board[row][col] = "X"