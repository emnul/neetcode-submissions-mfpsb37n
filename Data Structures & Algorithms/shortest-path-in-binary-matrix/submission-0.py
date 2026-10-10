class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        ROWS = COLS = len(grid)
        neighbors = [[1, 0], [-1, 0], [1, 1], [1, -1], [-1, -1], [-1, 1], [0, 1], [0, -1]]
        visit = set()
        q = collections.deque()

        q.append((0,0))
        visit.add((0,0))
        length = 1

        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                if row == ROWS - 1 and col == COLS - 1:
                    return length

                for dr, dc in neighbors:
                    newRow, newCol = row + dr, col + dc
                    
                    # check bounds
                    if (
                        min(newRow, newCol) < 0 or
                        newRow >= ROWS or
                        newCol >= COLS or
                        (newRow, newCol) in visit or
                        grid[newRow][newCol] == 1
                    ):
                        continue
                    # found neighbor
                    q.append((newRow, newCol))
                    visit.add((newRow, newCol))
            
            length += 1
        
        return -1
                

