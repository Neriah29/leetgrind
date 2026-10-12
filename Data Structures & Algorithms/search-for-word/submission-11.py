class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        def dfs(i, row, col):
            if i >= len(word):
                return True
            
            if not(0<= row < len(board) and 0<= col < len(board[0])) or word[i] != board[row][col]:
                return False

            temp = board[row][col]
            board[row][col] = "#"

            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            return any(dfs(i+1, row+dr, col + dc) for dr, dc in directions)
            board[row][col] = temp

            
            


        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if dfs(0, row, col):
                        return True 

        return False