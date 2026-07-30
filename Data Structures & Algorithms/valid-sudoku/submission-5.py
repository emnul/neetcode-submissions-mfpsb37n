class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * len(board)
        cols = [0] * len(board)
        squares = [0] * len(board)

        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == ".":
                    continue
                val = int(board[row][col])
                squareInd = ((row // 3) * 3 + (col // 3))

                if 1 << val & rows[row]:
                    return False
                if 1 << val & cols[col]:
                    return False
                if 1 << val & squares[squareInd]:
                    return False
                
                rows[row] |= 1 << val
                cols[col] |= 1 << val
                squares[squareInd] |= 1 << val
        
        return True