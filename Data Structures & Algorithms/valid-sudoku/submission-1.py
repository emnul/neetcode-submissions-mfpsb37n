from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [0] * 9
        rows = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                val = int(board[r][c]) - 1
                if (1 << val) & rows[r]:
                    return False
                if (1 << val) & cols[c]:
                    return False
                if (1 << val) & boxes[(r // 3) * 3 + (c // 3)]:
                    return False

                cols[c] |= 1 << val
                rows[r] |= 1 << val
                boxes[(r // 3) * 3 + (c // 3)] |= 1 << val
        return True
