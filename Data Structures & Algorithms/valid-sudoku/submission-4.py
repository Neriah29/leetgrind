class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        there are three rules to this.
        The rows, cols and boxes
        we are checking for in, we could use a set.
        I am thinking of using three dicts. 
        One for rows
        one for columns
        and one for boxes
        """

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board)):
                #check if there is a number
                num = board[row][col]
                box = (row//3, col//3)
                if num == ".": continue

                #check if the number is already in a row:
                if num in rows[row]:
                    return False
                else:
                    rows[row].add(num)
                
                #check if the number is already in a col
                if num in cols[col]:
                    return False
                else:
                    cols[col].add(num)
                
                #check for the boxes. We will label the boxes as coords of //
                if num in boxes[box]:
                    return False
                else:
                    boxes[box].add(num)
        
        return True