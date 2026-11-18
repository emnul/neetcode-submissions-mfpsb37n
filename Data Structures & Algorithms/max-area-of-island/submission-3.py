class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def bfs(r, c):
            q = deque([[r,c]])
            visited = set()
            area = 0

            while q:
                # process all elements currently in q
                row, col = q.popleft()

                # add lands connected to cur elem to q
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < ROWS and
                        0 <= nc < COLS and
                        (nr, nc) not in visited and
                        grid[nr][nc] == 1
                    ):
                        q.append([nr, nc])
                        visited.add((nr,nc))
                
                area += 1
                grid[row][col] = 0
            return area



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(bfs(r,c), maxArea)
        return maxArea


        