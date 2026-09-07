class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Find row of target using binary search
        l, r = 0, len(matrix) - 1
        row = None

        while l <= r:
            mid = (l + r) // 2
            print(matrix[mid])

            if target < matrix[mid][0]:
                r = mid - 1 
            elif target > matrix[mid][len(matrix[0]) - 1]:
                l = mid + 1
            else:
                row = mid
                break
        
        if row == None:
            return False
        
        # Find binary search within row to find target
        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            mid = (l + r) // 2

            if target < matrix[row][mid]:
                r = mid - 1 
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                return True
        
        return False
