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
        def dfs(row, col, p, visited):
            nonlocal flag
            if p >= len(word) or board[row][col] != word[p]:
                return
            if p == len(word)-1:
                flag = True
                return
            if row < len(board) - 1 and (row+1, col) not in visited:
                visited.add((row+1,col))
                dfs(row+1, col, p+1, visited)
                visited.remove((row+1,col))
            if row > 0 and (row-1, col) not in visited:
                visited.add((row-1,col))
                dfs(row - 1, col, p+1, visited)
                visited.remove((row-1, col))
            if col < len(board[row]) - 1 and (row, col+1) not in visited:
                visited.add((row, col+1))
                dfs(row, col + 1, p+1, visited)
                visited.remove((row,col+1))
            if col > 0 and (row, col-1) not in visited:
                visited.add((row, col-1))
                dfs(row, col - 1, p+1,visited)
                visited.remove((row, col-1))


        #iterate over every position. 
        #for every position, we run this dfs 
        for row in range(len(board)):
            for col in range(len(board[row])):
                if flag:
                    break
                if board[row][col] == word[0]:
                    dfs(row,col,0, {(row,col)})
        
        return flag
