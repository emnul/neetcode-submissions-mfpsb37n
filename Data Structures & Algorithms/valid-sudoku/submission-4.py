class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * len(board)
        cols = [0] * len(board)
        squares = [0] * len(board)

        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == ".":
                    continue
                
                val = int(board[r][c])
                sqInd = (r // 3 * 3 + c //3 )
                if (
                    1 << val & rows[r] or
                    1 << val & cols[c] or
                    1 << val & squares[sqInd]
                ):
                    return False
                
                rows[r] |= 1 << val
                cols[c] |= 1 << val
                squares[sqInd] |= 1 << val
        
        return True
                
