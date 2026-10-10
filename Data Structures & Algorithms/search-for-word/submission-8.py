class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        d = [(0,1), (0,-1), (1,0), (-1,0)]
        
        def rec(strInd, r, c):
            if board[r][c] != word[strInd]:
                return False
            if strInd == len(word)-1:
                return True
            oldChar = board[r][c]
            board[r][c] = '.'
            for dr, dc in d:
                nr,nc = r+dr, c+dc
                if nr<0 or nc < 0 or nr > len(board) or nc > len(board[0]):
                    continue
                if rec(strInd+1, nr, nc):
                    return True
            
            board[r][c] = oldChar
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if rec(0, row, col):
                    return True
        
        return False