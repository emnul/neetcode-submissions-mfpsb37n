class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        neighbors = [[-1, 0], [1,0], [0, 1], [0, -1]]
        fresh = time = 0
        q = collections.deque() # r,c,mins

        for row in range(ROWS):
            for col in range(COLS):
                # enq rotten oranges for BFS
                if grid[row][col] == 2:
                    q.append((row,col))
                # track fresh oranges
                if grid[row][col] == 1:
                    fresh += 1

                    
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in neighbors:
                    newRow, newCol = dr + r, dc + c

                    if (
                        min(newRow,newCol) < 0 or
                        newRow >= ROWS or
                        newCol >= COLS or
                        grid[newRow][newCol] != 1
                    ):
                        continue

                    grid[newRow][newCol] = 2
                    q.append((newRow, newCol))
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1




