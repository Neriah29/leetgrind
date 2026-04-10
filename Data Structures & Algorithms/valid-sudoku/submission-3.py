class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Approach:
        #create three hashmaps, for rows, columns and a 3x3 square
        # each of the values of the hashmaps will be hashsets
        #loop for each row and each column - 0(n^2)
        #check if that value is already part of the value for that row
        #in the row map, and do likewise for the rest
        #if there are any discrepancies, return False
        #After all the loops, it means no error was found 
        #so return true 

        #hashmap initialization
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        boxMap = defaultdict(set)

        #begin the loop
        for row in range(len(board)):
            for col in range(len(board)):
                curr = board[row][col]
                if curr == ".":
                    continue
                elif curr in rowMap[row] or curr in colMap[col] or curr in boxMap[(row//3, col//3)]:
                    return False
                rowMap[row].add(curr)
                colMap[col].add(curr)
                boxMap[(row//3, col//3)].add(curr)
        
        return True

                