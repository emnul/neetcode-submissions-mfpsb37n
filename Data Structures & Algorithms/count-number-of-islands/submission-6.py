class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1,0], [0, 1], [0, -1]] # up,down, left,right
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                # run bfs everytime we hit a piece of land
                # 0 land after processing
                # inc res
                if grid[r][c] == "1":
                    q = deque([[r, c]])
                    visted = set((r,c))

                    while q:
                        row, col = q.popleft()
                        # add valid adjacent lands to q
                        for dr, dc in directions:
                            newRow, newCol = row + dr, col + dc
                            if (0 <= newRow < ROWS and 
                                0 <= newCol < COLS and
                                (newRow, newCol) not in visted and
                                grid[newRow][newCol] == "1"
                            ):
                                q.append([newRow, newCol])
                                visted.add((newRow, newCol))
        
                        # mark land as processed
                        grid[row][col] = "0"
                    
                    res += 1
                            
        return res
