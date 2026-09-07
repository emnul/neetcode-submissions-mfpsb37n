class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, l, r = 0, 0, len(matrix[0]) - 1

        while l <= r and row <= len(matrix) - 1:
            if target > matrix[row][r]:
                row += 1
                continue
            
            mid = (l + r) // 2

            if target < matrix[row][mid]:
                r = mid - 1
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                return True
        
        return False
