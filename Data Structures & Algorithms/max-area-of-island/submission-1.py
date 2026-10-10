class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r,c):
            size = 1

            q = collections.deque()
            q.append((r,c))
            grid[r][c] = 0

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    newRow, newCol = row + dr, col + dc
                    if (
                        min(newRow, newCol) < 0 or
                        newRow >= ROWS or
                        newCol >= COLS or
                        grid[newRow][newCol] == 0
                    ):
                        continue
                    q.append((newRow, newCol))
                    grid[newRow][newCol] = 0
                    size += 1
            return size

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    size = bfs(r,c)
                    maxArea = max(size, maxArea)
        
        return maxArea
