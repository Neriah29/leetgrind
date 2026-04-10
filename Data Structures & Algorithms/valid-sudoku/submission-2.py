from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def is_duplicate(array):
            dupl_dict = defaultdict(int)
            for element in array:
                dupl_dict[element] += 1
            for key, value in dupl_dict.items():
                if key!= "." and value > 1:
                    return True 
            return False

        def row_valid(board):
            for row_idx in range(len(board)):
                if is_duplicate(board[row_idx]):
                    return False
            return True

        def col_valid(board):
            for col in range(len(board)):
                col_list =[]
                for row in range(len(board)):
                    col_list.append(board[row][col])
                    if is_duplicate(col_list):
                        return False
            return True

        def square_valid(square_list):
            if is_duplicate(square_list):
                return False
            return True
                    
        def all_square_valid(board):
            for first_col in range(0, len(board), 3):
                for first_row in range(0, len(board), 3):
                    square_list = []
                    for sq_col in range(first_col, first_col+3):
                        for sq_row in range(first_row, first_row +3):
                            square_list.append(board[sq_col][sq_row])
                    if not square_valid(square_list):
                        return False
            return True

        if row_valid(board) and col_valid(board) and all_square_valid(board):
            return True 
        return False


        